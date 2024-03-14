import json
import requests
import os
import re
import time

url = "myshopify.com/admin/api/2023-01/products.json?limit=250"
payload = {}
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": "",
}

column = ''
dir_path = os.path.dirname(os.path.realpath(__file__))

# Lista para almacenar todas las consultas SQL
all_variants_sql = []
# Lista para almacenar los SKU ya procesados
processed_skus = []

# Página inicial
page_info = ""

for i in range(1, 21):
    # Construir la URL de la solicitud
    request_url = url
    if page_info:
        request_url += f"&page_info={page_info}"
    # Agregar el enlace de la próxima página al header
    next_link = f'<{request_url}>; rel="next"'
    headers["Link"] = next_link

    # Obtener los headers de la respuesta para obtener la page_info de la próxima página

    response_headers = None
    while not response_headers:
        response = requests.request(
            "GET", request_url, headers=headers, data=payload)
        while not response.ok:
            print(f"Error en la petición, intentando nuevamente en 5 segundos...")
            time.sleep(5)
            response = requests.request(
                "GET", request_url, headers=headers, data=payload
            )

        response_headers = response.headers
        url = ""

        if "Link" in response_headers:
            link_header = response_headers["Link"]
            if 'rel="next"' in link_header:
                newUrl = link_header.replace("<", "").replace(">", "")
                url = re.sub(r"\brel=\"next\"\b", "", newUrl)
                page_info = ""
            else:
                page_info = ""
        else:
            print("Link header not found.")

    # Procesar la respuesta
    json_response = response.json()
    all_variants = []
    for product in json_response["products"]:
        all_variants += product["variants"]

    # Generar los scripts SQL para la variable all_variants
    for variant in all_variants:
        product_id = variant["product_id"]
        sku = variant["sku"]

        # Verificar si el SKU ya se ha procesado antes
        if sku in processed_skus:
            print(
                f"El SKU '{sku}' ya fue encontrado, no se agregará a la consulta SQL."
            )
        else:
            all_variants_sql.append(
                f"UPDATE products SET {column} = '{product_id}' WHERE sku = '{sku}';"
            )
            processed_skus.append(sku)


# Escribir todas las consultas SQL en un archivo .sql
with open(os.path.join(dir_path, "update/productos.sql"), "w") as f:
    f.write("\n".join(all_variants_sql))


print(f"Se generaron {len(all_variants_sql)} consultas SQL")
