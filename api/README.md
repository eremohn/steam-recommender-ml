# 🌐 Carpeta: api/

Esta carpeta contiene prototipos y desarrollo preliminar para exponer el sistema de recomendación como una **API REST**.

Actualmente se trabaja en notebooks de prueba para definir cómo estructurar y servir el modelo de recomendación.

---

## 📁 Contenido

| Archivo | Descripción |
|--------|-------------|
| `Desarrollo_API.ipynb` | Notebook exploratorio con pruebas para convertir el modelo en un servicio API. Incluye ideas para usar Flask o FastAPI. |

---

## 🎯 Objetivo

El propósito de esta carpeta es construir una interfaz que permita:

- Enviar una solicitud con el nombre o ID de un juego.
- Recibir recomendaciones de juegos similares como respuesta.
- (Opcional) Integrar con una interfaz web (ej. Streamlit) en el futuro.

---

## 🛠️ Estado actual

✔️ Exploración inicial en notebook.  
❌ Aún no hay endpoints implementados.  
🔄 Próximos pasos: migrar lógica a `app.py` con FastAPI o Flask.

---

## 💡 Ideas en desarrollo

- Endpoint `GET /recommend?id=123` que devuelve juegos similares.
- Endpoint alternativo `GET /recommend?name=Portal`.
- Respuesta en formato JSON con título, género, y puntaje de similitud.

---

## 🚀 Futuro inmediato

- Crear un archivo `app.py` que exponga los endpoints básicos.
- Probar localmente la API con `uvicorn` o `flask run`.
- Añadir validaciones y control de errores (ID no encontrado, nombre inválido, etc.).
- Preparar un `requirements_api.txt` con dependencias mínimas.

---

## 📌 Notas

- Esta carpeta crecerá con módulos reutilizables y test unitarios.
- La documentación será actualizada conforme se avance con el desarrollo real de la API.
