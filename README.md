# SteamRecommenderSystem

## Descripción
Este proyecto tiene como objetivo desarrollar un sistema de recomendación de videojuegos para la plataforma Steam utilizando técnicas de aprendizaje automático. Se emplea un proceso de Extracción, Transformación y Carga (ETL) para limpiar y normalizar los datos de tres fuentes principales:

- `australian_user_reviews.json`
- `australian_users_items.json`
- `output_steam_games.json`

Luego, se realiza un análisis exploratorio de datos (EDA) para comprender mejor la información disponible y se construye un modelo de machine learning para generar recomendaciones personalizadas basadas en las preferencias de los usuarios.

Se propone disponibilizar los datos usando el framework FastAPI, para responder a las siguientes consultas:

- Cantidad de items y porcentaje de contenido gratuito por año, según la empresa desarrolladora.
- Cantidad de dinero gastado por el usuario, el porcentaje de recomendaciones basado en reseñas y la cantidad de items que consume el mismo.
- Determinar el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
- Devolver el top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.
- Devolver la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

Finalizado este proceso, se implementa un modelo de aprendizaje automático que brinda un sistema de recomendación. El modelo responde a una relación ítem-ítem, es decir, toma un ítem y recomienda otros similares basados en su similitud.

## Alcance
- Preprocesamiento de datos utilizando ETL para limpiar y normalizar los conjuntos de datos.
- Análisis exploratorio de datos para comprender las características de los usuarios y los juegos.
- Disponibilización de los datos de la empresa usando el framework FastAPI.
- Construcción de un modelo de aprendizaje automático para generar recomendaciones personalizadas.
- Generación de visualizaciones para comunicar los hallazgos del análisis de datos.

## Dependencias
- Python 3.x
- pandas
- os
- fastapi
- scikit-learn
- matplotlib
- re
- json
- textblob

(Todas las dependencias necesarias se encuentran en el archivo `requirements.txt`)

## Datos
Para este proyecto se proporcionaron tres archivos JSON:

- `australian_user_reviews.json`: dataset que contiene comentarios de usuarios sobre los juegos, así como datos adicionales como la recomendación del juego, emoticones de y estadísticas de utilidad del comentario.
- `australian_users_items.json`: dataset que contiene información sobre los productos que juegan los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.
- `output_steam_games.json`: dataset que contiene datos relacionados con los juegos en sí, como título, desarrollador, precios, características técnicas, etiquetas, entre otros datos.

En el documento "Diccionario de datos" se encuentran los detalles de cada una de las variables de los conjuntos de datos.

## Tareas desarrolladas

### Transformaciones
Se realizó la extracción, transformación y carga (ETL) de los tres conjuntos de datos entregados, los cuales se encuentran en la carpeta `ETL`. Dos de los conjuntos de datos se encontraban anidados, es decir, había columnas con diccionarios o listas de diccionarios. Se aplicaron distintas estrategias para transformar las claves de esos diccionarios en columnas. Luego, se rellenaron algunos nulos de variables necesarias para el proyecto y se borraron columnas con muchos nulos o que no aportaban al proyecto, para optimizar el rendimiento de la API y teniendo en cuenta las limitaciones de almacenamiento del deploy. Para las transformaciones se utilizó la librería Pandas.

### Feature engineering
Se realizó un análisis de sentimiento a los reviews de los usuarios. Se creó una nueva columna llamada 'sentiment_analysis' que reemplaza a la columna que contiene los reviews, donde clasifica los sentimientos de los comentarios en una escala de 0 a 2, representando negativo, neutral o positivo, respectivamente. Este análisis se realizó utilizando TextBlob, una biblioteca de procesamiento de lenguaje natural (NLP) en Python.

### Análisis exploratorio de los datos
Se realizó un EDA al conjunto de datos con la finalidad de poder comprender el comportamiento de cada uno de ellos, antes de realizar las tareas de modelado y análisis más avanzados. En la carpeta `EDA` se encuentran los análisis exploratorios de los datos orientados a cada uno de las bases de datos, además de algunas métricas que muestran en perspectiva cómo se están comportando los datos.

### Modelo de aprendizaje automático
Se creó un modelo de aprendizaje automático que se encuentra en formato Python dentro de la carpeta `recomendacion_juego`. Este modelo tiene como función recibir un juego (item_id) y recomendar otros cinco juegos (títulos). Se utiliza el algoritmo k-NN con similitud coseno y el método de "fuerza bruta" para entrenar el modelo. Este modelo calcula la similitud entre los juegos basándose en la similitud coseno de sus vectores de características.

### Desarrollo de API
Para el desarrollo de la API se utilizó el framework FastAPI. Se crearon las siguientes funciones:

- `developer`: devuelve la cantidad de items y porcentaje de contenido gratuito por año según la empresa desarrolladora.
- `userdata`: devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendaciones basado en reseñas y la cantidad de items que consume el mismo.
- `UserForGenre`: devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
- `best_developer_year`: devuelve el top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.
- `developer_reviews_analysis`: devuelve el nombre del desarrollador con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

El desarrollo de las funciones de consultas generales se puede ver en el archivo `Desarrollo_API.ipynb`.

El código para generar la API se encuentra en el archivo `main.py` y las funciones para su funcionamiento se encuentran en `requirements.txt`. Para ejecutar la API desde localHost, se deben seguir los siguientes pasos:

1. Clonar el proyecto haciendo `git clone https://github.com/eremohn/SteamRecommenderSystem.git`.
2. Preparar el entorno de trabajo en Visual Studio Code:
   - Crear entorno Python: `python -m venv venv`
   - Ingresar al entorno: `venv\Scripts\activate`
   - Instalar dependencias: `pip install -r requirements.txt`
   - Ejecutar el archivo `main.py` desde consola activando `uvicorn`: `uvicorn main:app --port 5000 --reload`
3. Hacer clic sobre la dirección [http://XXX.X.X.X:XXXX](http://XXX.X.X.X:XXXX) (se muestra en la consola).
4. Una vez en el navegador, agregar `/docs` para acceder a ReDoc.
5. En cada una de las funciones, hacer clic en "Try it out" y luego introducir el dato que requiera o utilizar los ejemplos por defecto. Finalmente, ejecutar y observar la respuesta.

### Despliegue
Para el despliegue de la API se seleccionó la plataforma Render, que es una nube unificada para crear y ejecutar aplicaciones y sitios web, permitiendo el despliegue automático desde GitHub. El servicio queda corriendo en [https://steamrecommendersystem.onrender.com/docs](https://steamrecommendersystem.onrender.com/docs).

### Video
En el siguiente enlace se obtiene un video con una breve explicación del funcionamiento de la API.

---

## Fuente de Datos

**Dataset:** [Carpeta con los archivos que requieren ser procesados](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj). Tengan en cuenta que algunos datos están anidados (un diccionario o una lista como valores en la fila).

**Diccionario de Datos:** [Diccionario con algunas descripciones de las columnas disponibles en el dataset](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link).
