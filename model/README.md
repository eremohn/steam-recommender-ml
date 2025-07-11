# 🧠 Carpeta: model/

Esta carpeta contiene los scripts responsables de construir el sistema de recomendación de videojuegos basado en similitud entre juegos de la plataforma Steam.

---

## 📁 Archivo principal

| Archivo | Descripción |
|--------|-------------|
| `item_item_knn.py` | Implementa un modelo de recomendación basado en contenido utilizando TF‑IDF y el algoritmo K‑Nearest Neighbors. Permite obtener juegos similares a uno dado, en base a sus géneros y etiquetas. |

---

## 🔍 Descripción general del modelo

El enfoque actual es un **recomendador item-item** basado en contenido. Los pasos incluyen:

1. **Carga de datos** desde `data/processed/csv/output_steam_games.csv`.
2. **Preprocesamiento** de las columnas `genres` y `tags`, combinándolas para formar descripciones textuales.
3. **Vectorización TF‑IDF** de esas descripciones.
4. **Entrenamiento del modelo KNN** utilizando **similitud coseno**.
5. **Generación de recomendaciones** para un juego determinado.

---

## ▶️ Cómo usar

Desde la raíz del proyecto:

```bash
python model/item_item_knn.py --id 123 --top 5
```

O bien, podés importar el módulo en un notebook para usarlo de forma programática.

ℹ️ Para usar por nombre de juego, asegurate de que el campo app_name esté disponible en el dataset y sin errores de capitalización.

## ⚠️ Requisitos
- Python 3.8+

- pandas

- scikit-learn

Instalá las dependencias desde el archivo raíz del proyecto:
```
pip install -r requirements.txt

```

## 📌 Notas
- Este modelo no es supervisado y se recalcula en cada ejecución. Si el volumen de datos aumenta, podría considerarse persistir el modelo y el vectorizador.

- Ideal como punto de partida para futuras versiones con enfoques colaborativos, híbridos o basados en embeddings.
