# Generador de Consultas SQL para Productos Shopify

Este script en Python está diseñado para generar consultas SQL que permiten actualizar información de productos en una base de datos a partir de datos obtenidos de una tienda Shopify a través de su API.

## Funcionalidad Principal

El script realiza las siguientes acciones principales:

- **Obtención de Datos de Shopify:** Utiliza la API de Shopify para obtener información de productos y variantes desde una tienda específica.
- **Procesamiento de Datos:** Procesa la respuesta JSON de la API de Shopify para extraer información relevante, como IDs de producto y SKU de variantes.
- **Generación de Consultas SQL:** Genera consultas SQL para actualizar la base de datos local con la información obtenida de Shopify.
- **Escritura en Archivo SQL:** Escribe las consultas SQL generadas en un archivo .sql para su posterior ejecución en la base de datos.

## Componentes Principales

### Librerías Utilizadas:

- **json:** Para el manejo de datos en formato JSON.
- **requests:** Para realizar solicitudes HTTP a la API de Shopify.
- **os:** Para operaciones relacionadas con el sistema operativo, como la manipulación de rutas de archivo.
- **re:** Para realizar búsquedas y manipulaciones de cadenas utilizando expresiones regulares.
- **time:** Para introducir pausas entre intentos de solicitud en caso de errores.

### Variables Principales:

- **url:** La URL base de la API de Shopify.
- **payload:** Payload de la solicitud HTTP.
- **headers:** Encabezados de la solicitud HTTP, incluyendo el token de acceso a la API.
- **column:** Nombre de la columna en la base de datos donde se actualizarán los datos.
- **dir_path:** Ruta del directorio del script actual.

## Estructura del Script

- Utiliza un bucle for para iterar a través de las páginas de resultados de la API de Shopify.
- Maneja la paginación de la API utilizando el encabezado Link.
- Procesa los datos JSON obtenidos y genera consultas SQL para cada producto y variante.
- Escribe las consultas SQL en un archivo .sql.

## Ejecución y Resultados

Para ejecutar el script, simplemente ejecuta el archivo Python. Después de la ejecución, el script generará un archivo .sql en el directorio update/productos.sql con todas las consultas SQL necesarias para actualizar la base de datos con la información de productos de Shopify.

El script también imprimirá la cantidad total de consultas SQL generadas.

¡Usa este script para automatizar la actualización de información de productos de Shopify en tu base de datos de manera eficiente y sin esfuerzo manual!
