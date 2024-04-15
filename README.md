# SteamRecommenderSystem
## Desarrollo de un Sistema de Recomendación de Videojuegos para Steam

Este repositorio contiene una serie de scripts de Python diseñados para procesar y transformar datos de Steam para un proyecto de recomendación de videojuegos. Los scripts realizan tareas de extracción, transformación y carga (ETL) para preparar los datos para análisis y modelado posterior.

## Descripción del Proyecto

El objetivo principal de este proyecto es preparar un entorno de datos limpio y estructurado a partir de datos en bruto de Steam, que incluyen reseñas de usuarios y datos de juego. Estos datos son esenciales para desarrollar un sistema de recomendación de videojuegos eficiente, que pueda sugerir títulos de manera precisa a los usuarios de la plataforma.

## Características Principales de Proceso de ETL

Se encuentran tres archivos en formato Python diseñados específicamente para realizar tareas de Extracción, Transformación y Carga (ETL) sobre los datos proporcionados en la carpeta `Dataset`. A continuación se detallan las principales características y funcionalidades de cada archivo en formato Python:

- **Extracción de Datos:** Los archivos `user_reviews.csv`, `australian_users_items.csv` y `output_steam_games.csv` cargan los datos en formato CSV desde múltiples archivos ubicados en la carpeta `Dataset`. Estos archivos contienen información sobre usuarios, ítems de juego y reseñas de usuarios en la plataforma Steam.

- **Transformación de Datos:** Los archivos `user_reviews.csv`, `australian_users_items.csv` y `output_steam_games.csv` llevan a cabo un proceso exhaustivo de limpieza y transformación de los datos para corregir formatos y valores incorrectos. Esto incluye la conversión de los datos de CSV a un formato más manipulable y el análisis de sentimiento aplicado a las reseñas de usuarios para categorizarlas en positivas, negativas o neutras.

- **Carga de Datos:** Una vez transformados, los datos se guardan en formato CSV y parquet, permitiendo su fácil acceso y manipulación en etapas posteriores de análisis. Los archivos CSV se utilizan para almacenamiento convencional, mientras que los archivos parquet conservan la estructura y los tipos de datos de manera más eficiente.

Estos archivos son fundamentales para el desarrollo del sistema de recomendación de videojuegos y constituyen la base del análisis de datos subsiguiente.

## Uso

Cada script dentro del repositorio está diseñado para ser ejecutado de forma independiente, dependiendo de la necesidad específica de procesamiento de datos. Los usuarios pueden ejecutar cada script siguiendo las instrucciones de instalación y requisitos previos detallados en los comentarios del código.

## Contribuir

Se invita a otros desarrolladores a contribuir al proyecto mediante la creación de pull requests o la apertura de issues para discutir mejoras y nuevas funcionalidades.

---

## Fuente de Datos

**Dataset:** [Carpeta con los archivos que requieren ser procesados](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj). Tengan en cuenta que algunos datos están anidados (un diccionario o una lista como valores en la fila).

**Diccionario de Datos:** [Diccionario con algunas descripciones de las columnas disponibles en el dataset](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link).
