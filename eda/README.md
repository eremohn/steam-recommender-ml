# 📊 Carpeta: eda/

Esta carpeta contiene los notebooks de análisis exploratorio de datos (EDA) realizados sobre los datasets procesados.  
El objetivo del EDA es comprender mejor la estructura, calidad y relaciones entre las variables antes del desarrollo del modelo de recomendación.

---

## 📄 Descripción de los notebooks

Cada archivo .ipynb en esta carpeta analiza uno de los datasets procesados individualmente:

- `EDA_user_reviews.ipynb`:  
  Análisis de las reseñas de usuarios, distribución de opiniones, análisis de sentimientos y relación con otros atributos (horas jugadas, juegos favoritos, etc.).

- `EDA_output_steam_games.ipynb`:  
  Exploración de las características de los juegos: géneros, precios, fechas de lanzamiento, calificaciones, etiquetas, etc.

- `EDA_australian_users_items.ipynb`:  
  Análisis del comportamiento de usuarios australianos: historial de juegos, tiempo de juego, hábitos de compra, y patrones de interacción con los juegos.

---

## 🔧 Herramientas utilizadas

- `Pandas`: para manipulación tabular.
- `Matplotlib` y `Seaborn`: para visualización de distribuciones y relaciones.
- `WordCloud` (en algunos casos): para visualización de etiquetas y términos frecuentes.
- `NLTK` o `TextBlob` (opcional): para análisis de sentimiento básico.

---

## ⚙️ Requisitos

Para ejecutar estos notebooks, asegurate de haber corrido previamente los scripts ETL que generan los archivos en `data/processed/`.

Se recomienda ejecutar los notebooks en un entorno virtual con los paquetes definidos en `requirements.txt`.

---

## 📌 Notas

- Estos notebooks no deben modificar los datasets, sólo analizarlos.
- Sus insights se usan para guiar la ingeniería de características del modelo.
- Pueden ser referenciados en informes o documentación técnica del proyecto.

