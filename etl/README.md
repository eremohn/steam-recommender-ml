# 🛠️ Carpeta: etl/

Esta carpeta contiene los scripts de procesamiento de datos (ETL: Extract, Transform, Load) utilizados para limpiar, transformar y preparar los datasets originales en formato JSON.  
El resultado de este proceso son archivos estructurados en formato CSV y Parquet, que luego se utilizan para el análisis exploratorio (EDA) y el desarrollo del modelo de recomendación.

---

## 📄 Descripción de los scripts

Cada script corresponde a uno de los datasets originales:

- `etl_user_reviews.py`  
  - Limpia y normaliza las reseñas de usuarios.
  - Extrae y analiza sentimientos de los textos.
  - Elimina columnas innecesarias y corrige errores de formato.
  - Exporta: `user_reviews.csv` y `user_reviews.parquet`.

- `etl_output_steam_games.py`  
  - Limpia información de juegos: nombres, géneros, etiquetas, precios y fechas de lanzamiento.
  - Convierte datos categóricos y normaliza formatos de precios y fechas.
  - Exporta: `output_steam_games.csv` y `output_steam_games.parquet`.

- `etl_australian_users_items.py`  
  - Procesa información sobre usuarios australianos y sus juegos.
  - Desanida listas, corrige valores `NaN`, y transforma estructuras complejas.
  - Exporta: `australian_users_items.csv` y `australian_users_items.parquet`.

---

## 📂 Archivos de entrada esperados

Los scripts esperan que los archivos `.json` originales estén ubicados en la carpeta:

```
data/raw/
```

> ⚠️ Si no tenés estos archivos localmente, podés descargarlos desde el enlace compartido en el [`README.md`](../README.md) principal del proyecto.

---

## 📂 Archivos de salida generados

Los archivos procesados se guardan en:

```
data/processed/
├── csv/
└── parquet/

```


---

## ▶️ Cómo ejecutar los scripts

Desde la raíz del proyecto, ejecutá los siguientes comandos:

```bash
python etl/etl_user_reviews.py
python etl/etl_output_steam_games.py
python etl/etl_australian_users_items.py
```
Esto generará los archivos listos para el análisis exploratorio y modelado.

## 📌 Notas adicionales
Cada script es autónomo, pero pueden ejecutarse en cualquier orden.

No se recomienda editar manualmente los archivos generados.

El código está pensado para ser legible y fácilmente ampliable con validaciones o mejoras futuras.





