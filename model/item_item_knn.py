import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

# Cargar los datos
user_reviews = pd.read_csv('user_reviews.csv')
steam_games = pd.read_csv('output_steam_games.csv')

# Preprocesamiento de datos (si es necesario)
# Combinar las características de texto en una sola cadena y manejar los valores NaN
steam_games['combined_features'] = steam_games['genres'].fillna('') + ' ' + steam_games['tags'].fillna('')

# Definir la matriz de características
vectorizer = TfidfVectorizer()
caracteristicas = vectorizer.fit_transform(steam_games['combined_features'])

# Entrenamiento del modelo
model = NearestNeighbors(metric='cosine', algorithm='brute')  # Usar similitud coseno y el algoritmo de fuerza bruta
model.fit(caracteristicas)

# Función para obtener recomendaciones
def get_recommendations(item_id, k=5):
    # Encontrar los índices de los vecinos más cercanos
    distances, indices = model.kneighbors(caracteristicas[item_id], n_neighbors=k+1)
    # Excluir el propio juego de las recomendaciones
    indices = indices[:, 1:]
    return indices.flatten()

# Ejemplo de uso
juego_id = 123  # Aquí debes proporcionar el ID del juego para el que deseas obtener recomendaciones
recomendaciones = get_recommendations(juego_id)
print("Recomendaciones para el juego", juego_id, ":")
for i, juego_idx in enumerate(recomendaciones):
    print(i+1, ".", steam_games.iloc[juego_idx]['app_name'])
