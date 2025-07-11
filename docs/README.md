# 📄 Informe Técnico del Proyecto: Sistema de Recomendación de Juegos para Steam

Este documento resume el desarrollo de un sistema de recomendación de videojuegos basado en técnicas de Machine Learning. El objetivo es ofrecer recomendaciones personalizadas de juegos dentro de la plataforma Steam, a partir del análisis de datos reales de usuarios.

---

## 🧩 Estructura del Proyecto

El desarrollo se divide en tres etapas principales:

1. **Procesamiento de datos (ETL)**
2. **Análisis exploratorio (EDA)**
3. **Modelado y generación de recomendaciones**

---

## 🔄 Procesamiento de Datos (ETL)

Se desarrollaron tres scripts en Python para procesar los datos crudos, provenientes de archivos `.json` con estructuras anidadas.

### Archivos originales utilizados

- `australian_user_reviews.json`
- `australian_users_items.json`
- `output_steam_games.json`

### Funcionalidad de los scripts

- **`etl_user_reviews.py`**
  - Corrige errores de formato.
  - Normaliza tipos de datos.
  - Elimina columnas irrelevantes.
  - Aplica análisis de sentimiento a los textos.
  - Exporta a CSV y Parquet.

- **`etl_output_steam_games.py`**
  - Elimina filas vacías.
  - Renombra columnas para facilitar el análisis.
  - Convierte precios a `float` y fechas a `datetime`.
  - Exporta a CSV y Parquet.

- **`etl_australian_users_items.py`**
  - Desanida estructuras tipo listas y diccionarios.
  - Convierte strings a listas.
  - Maneja valores nulos.
  - Exporta a CSV y Parquet.

Los datos limpios se almacenan en la carpeta `data/processed/`.

---

## 📊 Análisis Exploratorio (EDA)

Se realizó un estudio detallado de cada dataset procesado con el fin de comprender su estructura, calidad y relaciones internas.

### Principales acciones

- Identificación de valores atípicos y faltantes.
- Estadísticas descriptivas generales.
- Visualización de:
  - Distribuciones de variables numéricas.
  - Frecuencia de géneros y etiquetas de juegos.
  - Relación entre horas jugadas y calificación.
  - Sentimientos extraídos de las reseñas.

Los notebooks se encuentran en la carpeta `eda/`.

---

## 🤖 Modelo de Recomendación

Se implementó un sistema de recomendación **basado en contenido**, usando el algoritmo **K-Nearest Neighbors (KNN)** y similitud **coseno**.

### Características del modelo

- Extracción de características relevantes (géneros, etiquetas, etc.).
- Representación vectorial de los juegos.
- Búsqueda de vecinos más similares en el espacio vectorial.
- Retorno de juegos similares a uno dado como entrada.

### Uso del modelo

El módulo `model/item_item_knn.py` permite obtener recomendaciones personalizadas mediante una función simple que recibe el nombre de un juego y devuelve sugerencias similares.

---

## ✅ Conclusiones

El sistema desarrollado permite generar recomendaciones de juegos de forma automática, utilizando datos reales y técnicas de machine learning.  
El enfoque basado en contenido es efectivo y sirve como punto de partida para probar variantes más avanzadas, como:

- Filtrado colaborativo.
- Modelos híbridos.
- Representaciones basadas en embeddings.

---

📁 Este archivo reemplaza al antiguo PDF del informe, y centraliza la documentación técnica del proyecto.

