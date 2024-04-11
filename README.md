# SteamRecommenderSystem
## Desarrollo de un Sistema de Recomendación de Videojuegos para Steam

Este repositorio contiene una serie de scripts de ipynb diseñados para procesar y transformar datos de Steam para un proyecto de recomendación de videojuegos. Los scripts realizan tareas de extracción, transformación y carga (ETL) para preparar los datos para análisis y modelado posterior.

## Descripción del Proyecto

El objetivo principal de este proyecto es preparar un entorno de datos limpio y estructurado a partir de datos en bruto de Steam, que incluyen reseñas de usuarios y datos de juego. Estos datos son esenciales para desarrollar un sistema de recomendación de videojuegos eficiente, que pueda sugerir títulos de manera precisa a los usuarios de la plataforma.

## Características Principales de Proceso_de_ETL.ipynb

El archivo `Proceso_de_ETL.ipynb` es un cuaderno Jupyter diseñado para realizar tareas de Extracción, Transformación y Carga (ETL) sobre los datos proporcionados en la carpeta `Dataset`. A continuación se detallan las principales características y funcionalidades del cuaderno:

- **Extracción de Datos:** El cuaderno carga datos en formato JSON desde múltiples archivos ubicados en la carpeta `Dataset`. Estos archivos contienen información sobre usuarios, ítems de juego y reseñas de usuarios en la plataforma Steam.

- **Transformación de Datos:** El cuaderno lleva a cabo un proceso exhaustivo de limpieza y transformación de los datos para corregir formatos y valores incorrectos. Esto incluye la conversión de los datos de JSON a CSV para su fácil manipulación y análisis posterior. Además, se aplica un análisis de sentimiento a las reseñas de usuarios para categorizarlas en positivas, negativas o neutras.

- **Carga de Datos:** Una vez transformados, los datos se guardan en formato CSV en los archivos `australian_users_items.csv`, `output_steam_games.csv` y `user_reviews.csv`, permitiendo su fácil acceso y manipulación en etapas posteriores de análisis.

Además de los archivos CSV mencionados, el cuaderno `Proceso_de_ETL.ipynb` también genera archivos Parquet para cada conjunto de datos transformado. Estos archivos se nombran como `australian_users_items.parquet`, `output_steam_games.parquet` y `user_reviews.parquet`, y proporcionan una opción de almacenamiento alternativa que conserva la estructura y los tipos de datos de manera más eficiente que los archivos CSV.

Una vez que se ha ejecutado el cuaderno `Proceso_de_ETL.ipynb` sobre los conjuntos de datos proporcionados en la carpeta `Dataset`, se obtienen los archivos mencionados anteriormente. Estos archivos son fundamentales para el desarrollo del sistema de recomendación de videojuegos y constituyen la base del análisis de datos subsiguiente.


## Uso

Cada script dentro del repositorio está diseñado para ser ejecutado de forma independiente, dependiendo de la necesidad específica de procesamiento de datos. Los usuarios pueden ejecutar cada script siguiendo las instrucciones de instalación y requisitos previos detallados en los comentarios del código.

## Contribuir

Se invita a otros desarrolladores a contribuir al proyecto mediante la creación de pull requests o la apertura de issues para discutir mejoras y nuevas funcionalidades.

---

## Fuente de Datos

**Dataset:** [Carpeta con los archivos que requieren ser procesados](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj), tengan en cuenta que hay datos que están anidados (un diccionario o una lista como valores en la fila).

**Diccionario de datos:** [Diccionario con algunas descripciones de las columnas disponibles en el dataset](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link).
