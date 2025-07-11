# 🧠 Carpeta: model/

Esta carpeta contiene los scripts relacionados con la construcción del modelo de recomendación de videojuegos para Steam. El enfoque utilizado en esta primera versión es un **recomendador basado en contenido** que emplea el algoritmo de **vecinos más cercanos (K-Nearest Neighbors, KNN)** y **similitud coseno**.

---

## 📁 Archivo principal

- `item_item_knn.py`:  
  Script principal del modelo. Permite obtener juegos similares a uno dado, en base a sus características (géneros, etiquetas, etc.).

---

## 🔍 Descripción del modelo

El sistema analiza las características de los juegos y construye un espacio vectorial para calcular similitudes entre ellos. Se utiliza un modelo `KNN` entrenado con métricas de similitud coseno para encontrar los juegos más cercanos.

### Pasos generales:

1. **Carga de datos procesados** desde `data/processed/csv/output_steam_games.csv`.
2. **Preprocesamiento y vectorización** de los campos relevantes (por ejemplo: `tags`, `genres`, etc.).
3. **Cálculo de similitud coseno** entre vectores de juegos.
4. **Generación de recomendaciones** para un juego de entrada.

---

## 🧪 Ejemplo de uso

Dentro del script hay una función principal:

```python
def recomendar_juegos(nombre_juego, n=5):
    ...
    return recomendaciones
```
Esta función toma como entrada el nombre de un juego (string) y devuelve una lista de n juegos similares.

## ⚠️ Requisitos
Asegurate de ejecutar previamente los scripts ETL, ya que este módulo depende del archivo:

```
data/processed/csv/output_steam_games.csv

```
## 📌 Notas
El modelo es fácilmente extensible a otros enfoques (colaborativo, híbrido, embeddings).

No se requiere entrenamiento tradicional: el modelo es no supervisado y se basa en similitud entre características.

Esta versión es item-item, pero se puede adaptar a un sistema user-item si se dispone de ratings o historiales de usuario.

