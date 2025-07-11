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
Contiene los datos originales obtenidos del dataset público.  
Estos archivos no han sido modificados manualmente y se usan como entrada para los scripts de limpieza (ETL).

Ejemplos:
- `australian_users_items.json`
- `user_reviews.json`
- `output_steam_games.json`

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
