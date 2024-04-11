# SteamRecommenderSystem
## Desarrollo de un Sistema de Recomendación de Videojuegos para Steam

Este repositorio contiene una serie de scripts de Python diseñados para procesar y transformar datos de Steam para un proyecto de recomendación de videojuegos. Los scripts realizan tareas de extracción, transformación y carga (ETL) para preparar los datos para análisis y modelado posterior.

## Descripción del Proyecto

El objetivo principal de este proyecto es preparar un entorno de datos limpio y estructurado a partir de datos en bruto de Steam, que incluyen reseñas de usuarios y datos de juego. Estos datos son esenciales para desarrollar un sistema de recomendación de videojuegos eficiente, que pueda sugerir títulos de manera precisa a los usuarios de la plataforma.

## Características Principales

- **Extracción de Datos:** Carga datos en formato JSON desde múltiples archivos.
- **Transformación de Datos:** Limpia y transforma datos para corregir formatos y valores incorrectos. Incluye la conversión de datos de JSON a CSV, y la aplicación de análisis de sentimiento a las reseñas de usuarios.
- **Carga de Datos:** Los datos transformados se guardan en formato CSV para su fácil acceso y manipulación en etapas posteriores de análisis.

## Uso

Cada script dentro del repositorio está diseñado para ser ejecutado de forma independiente, dependiendo de la necesidad específica de procesamiento de datos. Los usuarios pueden ejecutar cada script siguiendo las instrucciones de instalación y requisitos previos detallados en los comentarios del código.

## Contribuir

Se invita a otros desarrolladores a contribuir al proyecto mediante la creación de pull requests o la apertura de issues para discutir mejoras y nuevas funcionalidades.

---

## Fuente de Datos

**Dataset:** [Carpeta con los archivos que requieren ser procesados](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj), tengan en cuenta que hay datos que están anidados (un diccionario o una lista como valores en la fila).

**Diccionario de datos:** [Diccionario con algunas descripciones de las columnas disponibles en el dataset](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link).
