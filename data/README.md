# 📂 Carpeta: data/

Esta carpeta contiene los archivos de datos utilizados durante el desarrollo del sistema de recomendación de videojuegos.

Está organizada en subcarpetas que separan los archivos según su grado de procesamiento:

---

## 📁 Estructura

```
data/
├── raw/ # Archivos originales en formato CSV, JSON o Parquet
├── processed/ # Datos limpios generados por los scripts ETL
```

---

## 📄 Descripción de subcarpetas


### 🔸 `raw/`  
Esta carpeta **no contiene archivos actualmente** debido al gran tamaño de los datos originales.  
Sin embargo, estos pueden ser descargados desde el siguiente enlace compartido en el `README.md` principal del repositorio:

📁 **[Carpeta de datos original (Google Drive)](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)**

> Una vez descargados, colocá los archivos `.json` dentro de esta carpeta para ejecutar el pipeline ETL.


### 🔸 `processed/`
Contiene los datos transformados por los scripts ETL.  
Aquí se almacenan los archivos ya normalizados y listos para el análisis y modelado.

Ejemplos:
- `australian_users_items.csv`
- `user_reviews.parquet`
- `output_steam_games.csv`

---

## ⚠️ Nota

Los archivos de esta carpeta no deben ser editados manualmente.  
Cualquier cambio debe realizarse a través de los scripts del pipeline ETL ubicados en la carpeta [`etl/`](../../etl/).

---

## 📌 Recomendación

Se recomienda mantener esta estructura para asegurar la reproducibilidad del pipeline completo.  
Los scripts y notebooks del proyecto están diseñados para trabajar directamente con estos directorios.
