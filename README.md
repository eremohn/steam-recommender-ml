# SteamRecommenderSystem
## Descripción
Este proyecto tiene como objetivo desarrollar un sistema de recomendación de videojuegos para la plataforma Steam utilizando técnicas de aprendizaje automático. Se emplea un proceso de Extracción, Transformación y Carga (ETL) para limpiar y normalizar los datos de tres fuentes principales:

- `australian_user_reviews.json`
- `australian_users_items.json`
- `output_steam_games.json`

Luego, se realiza un análisis exploratorio de datos (EDA) para comprender mejor la información disponible y se construye un modelo de machine learning para generar recomendaciones personalizadas basadas en las preferencias de los usuarios.

## Alcance
- Preprocesamiento de datos utilizando ETL para limpiar y normalizar los conjuntos de datos.
- Análisis exploratorio de datos para comprender las características de los usuarios y los juegos.
- Construcción de un modelo de aprendizaje automático para generar recomendaciones personalizadas.
- Generación de visualizaciones para comunicar los hallazgos del análisis de datos.

## Dependencias
- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Créditos
Este proyecto es desarrollado por Felipe Varela(eremohn). Cualquier pregunta o comentario es bienvenido.

## Licencia
Este proyecto está bajo la [Licencia MIT](LICENSE).

---

## Fuente de Datos

**Dataset:** [Carpeta con los archivos que requieren ser procesados](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj). Tengan en cuenta que algunos datos están anidados (un diccionario o una lista como valores en la fila).

**Diccionario de Datos:** [Diccionario con algunas descripciones de las columnas disponibles en el dataset](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link).
