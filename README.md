# 🎮 Steam Recommender ML

Este proyecto desarrolla un sistema de recomendación de videojuegos para la plataforma Steam, utilizando técnicas de machine learning. Se basa en datos públicos de usuarios australianos y aplica procesamiento de datos, análisis exploratorio, análisis de sentimientos y un modelo de recomendación basado en similitud entre juegos.

---



## 📌 Tabla de contenidos

- [📄 Descripción del proyecto](#-descripción-del-proyecto)
- [🔗 Fuente de Datos](#-fuente-de-datos)
- [📁 Estructura del repositorio](#-estructura-del-repositorio)
- [🚀 Cómo ejecutar el proyecto](#-cómo-ejecutar-el-proyecto)
- [⚙️ Detalles técnicos](#-detalles-técnicos)
- [✅ Resultados esperados](#-resultados-esperados)
- [📈 Próximos pasos](#-próximos-pasos)
- [📝 Licencia](#-📝-licencia)
- [🤝 Autor](#-🤝-autor)

---

## 📄 Descripción del proyecto

El objetivo principal es crear un sistema que recomiende juegos de Steam similares entre sí a partir de sus características y preferencias de los usuarios. Para lograrlo, se desarrolló un pipeline completo que incluye:

- Procesamiento y limpieza de datos desde archivos JSON anidados.
- Análisis exploratorio de los datos procesados.
- Extracción de sentimientos desde reseñas de usuarios.
- Modelo de machine learning basado en K-Nearest Neighbors con similitud coseno.
- Desarrollo preliminar de una API para ofrecer las recomendaciones.

---

## 🔗 Fuente de Datos

- **Dataset:** [Carpeta con los archivos que requieren ser procesados](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)  
  Contiene archivos JSON con estructuras anidadas (listas, diccionarios por fila) que deben ser tratados en la etapa de ETL.

- **Diccionario de Datos:** [Diccionario con algunas descripciones de las columnas disponibles en el dataset](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link)

---

## 📁 Estructura del repositorio
```bash

steam-recommender-ml/
├── data/
│ ├── raw/ # Datos originales en CSV/Parquet
│ └── processed/ # (Opcional) Datos limpios
│
├── eda/ # Análisis exploratorio
├── etl/ # Scripts ETL por dataset
├── model/ # Modelo de recomendación
├── api/ # Desarrollo API (WIP)
├── docs/ # Informe técnico
├── main.py # Ejecución principal
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/eremohn/steam-recommender-ml.git
cd steam-recommender-ml
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```
3. Ejecutar scripts de limpieza (ETL):

```bash
python etl/etl_user_reviews.py
python etl/etl_output_steam_games.py
python etl/etl_australian_users_items.py
```

4. Explorar los notebooks de análisis (eda/) o ejecutar el modelo desde model/item_item_knn.py


---

## ⚙️ Detalles técnicos

- Scripts ETL para convertir archivos JSON en CSV y Parquet, normalizando estructuras anidadas (listas, diccionarios).
- Análisis exploratorio utilizando Pandas, Matplotlib y Seaborn para entender la distribución y relaciones entre variables.
- Análisis de sentimiento básico aplicado a las reseñas de usuarios para enriquecer los datos.
- Sistema de recomendación basado en similitud coseno entre juegos, implementado con el algoritmo K-Nearest Neighbors (item-item).
- Desarrollo preliminar de una API para ofrecer las recomendaciones como servicio.

---

## ✅ Resultados esperados

- Generación de recomendaciones de juegos similares en base a un título de entrada.
- Análisis descriptivo y visual del comportamiento de los usuarios, juegos más populares, distribución de precios, géneros, etc.
- Base sólida para experimentar con modelos más avanzados de recomendación como filtrado colaborativo, LightFM, o embeddings personalizados.

---

## 📈 Próximos pasos

- Incorporar una API REST funcional con FastAPI o Flask para consumir recomendaciones.
- Crear una interfaz interactiva con Streamlit para probar el sistema desde el navegador.
- Evaluar el rendimiento del sistema con métricas como Precision@k, Recall@k o Mean Average Precision.
- Implementar versiones híbridas que combinen filtrado basado en contenido con comportamiento del usuario.

---

## 📝 Licencia

Este proyecto se encuentra bajo la Licencia MIT. Para más información, consultar el archivo [`LICENSE`](./LICENSE).

---

## 🤝 Autor

Proyecto desarrollado por **Felipe Varela**.
