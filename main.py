import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from typing import List
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()

# Obtener la ruta al directorio actual del script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas completas a los archivos CSV en el directorio "CSV"
user_reviews_path = os.path.join(directorio_actual, 'csv', 'user_reviews.csv')
output_steam_games_path = os.path.join(directorio_actual, 'csv', 'output_steam_games.csv')
australian_users_items_path = os.path.join(directorio_actual, 'csv', 'australian_users_items.csv')

# Cargar los datos desde los archivos CSV en las nuevas rutas
user_reviews = pd.read_csv(user_reviews_path)
output_steam_games = pd.read_csv(output_steam_games_path)
australian_users_items = pd.read_csv(australian_users_items_path)

# Cargar los datos y entrenar el modelo al iniciar la aplicación
steam_games = pd.read_csv(output_steam_games_path)  # Usamos la misma ruta para "output_steam_games.csv"
steam_games['combined_features'] = steam_games['genres'].fillna('') + ' ' + steam_games['tags'].fillna('')
vectorizer = TfidfVectorizer()
caracteristicas = vectorizer.fit_transform(steam_games['combined_features'])
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(caracteristicas)


@app.get('/')
def message():
    return "<h1 style='text-align: center; font-size: 32px;'>API de desarrolladores de juegos</h1><p style='text-align: center; font-size: 24px;'>Escriba /docs a continuación de la URL actual de esta página para interactuar con la API.</p>"

@app.get('/developer')
def developer(desarrollador: str):

    # Comprobar si el desarrollador proporcionado existe en los datos
    if desarrollador not in output_steam_games['developer'].unique():
        return {"error": "Desarrollador no encontrado"}

    # Filtrar los datos por desarrollador
    df = output_steam_games[output_steam_games['developer'] == desarrollador]

    # Convertir la columna 'release_date' a tipo datetime si es necesario
    if 'release_date' in df.columns:
        df['release_date'] = pd.to_datetime(df['release_date'])

    # Extraer el año de la fecha de lanzamiento si está presente
    if 'release_date' in df.columns:
        df['year'] = df['release_date'].dt.year

    # Determinar si el juego es gratuito o no según la columna 'tags'
    df['free'] = df['tags'].str.contains('Free', case=False)

    # Agrupar por año y desarrollador, y calcular la cantidad de items y el porcentaje de contenido free
    resultados = df.groupby(['year', 'developer']).agg(
        cantidad_de_items=('item_id', 'count'),
        contenido_free=('free', 'mean')  # Calculamos el porcentaje promedio de contenido free
    ).reset_index()

    # Formatear el porcentaje de contenido free como porcentaje
    resultados['contenido_free'] = (resultados['contenido_free'] * 100).round(2).astype(str) + '%'

    # Convertir los resultados a un diccionario para su retorno
    return resultados.to_dict(orient='records')



@app.get('/userdata')
def userdata(user_id: str):
    # Filtrar los datos por el ID de usuario
    user_items = australian_users_items[australian_users_items['user_id'] == user_id]
    
    # Fusionar los DataFrames para obtener el precio de cada juego que posee el usuario
    user_items_with_price = pd.merge(user_items, output_steam_games[['item_id', 'price']], on='item_id', how='left')
    
    # Calcular el dinero gastado por el usuario
    money_spent = user_items_with_price['price'].sum()
    
    # Calcular el porcentaje de recomendación promedio por usuario
    recommendation_percentage = user_reviews[user_reviews['user_id'] == user_id]['recommend'].mean() * 100
    
    # Contar la cantidad de items por usuario
    items_count = len(user_items)
    
    # Retornar los resultados
    return {
        "Usuario": user_id,
        "Dinero gastado": money_spent,
        "% de recomendación": recommendation_percentage,
        "Cantidad de items": items_count
    }



@app.get('/UserForGenre')
def UserForGenre(genero: str):
    # Filtrar los datos de australian_users_items por el género dado
    user_items_genre = australian_users_items[australian_users_items['item_name'].str.contains(genero, case=False, na=False)]
    
    # Agrupar por usuario y sumar las horas jugadas
    user_playtime = user_items_genre.groupby('user_id')['playtime_forever'].sum().reset_index()
    
    if user_playtime.empty:
        return {"error": "No se encontraron datos para el género proporcionado"}
    
    # Encontrar el usuario con más horas jugadas para el género dado
    max_playtime_user = user_playtime.loc[user_playtime['playtime_forever'].idxmax()]
    max_playtime_user_id = max_playtime_user['user_id']
    max_playtime = max_playtime_user['playtime_forever']
    
    # Filtrar los juegos del usuario con más horas jugadas para obtener el año de lanzamiento
    max_playtime_user_games = australian_users_items[(australian_users_items['user_id'] == max_playtime_user_id) & (australian_users_items['item_name'].str.contains(genero, case=False, na=False))]
    max_playtime_user_games = pd.merge(max_playtime_user_games, output_steam_games[['item_id', 'release_date']], on='item_id', how='left')
    
    # Convertir la columna 'release_date' a tipo datetime
    max_playtime_user_games['release_date'] = pd.to_datetime(max_playtime_user_games['release_date'])
    
    # Calcular la acumulación de horas jugadas por año de lanzamiento
    playtime_by_year = max_playtime_user_games.groupby(max_playtime_user_games['release_date'].dt.year)['playtime_forever'].sum().reset_index()
    playtime_by_year.rename(columns={'release_date': 'Año', 'playtime_forever': 'Horas'}, inplace=True)
    playtime_by_year = playtime_by_year.astype({'Año': int})
    playtime_by_year = playtime_by_year.to_dict(orient='records')
    
    # Retornar el usuario con más horas jugadas y la acumulación de horas jugadas por año de lanzamiento
    return {
        f"Usuario con más horas jugadas para Género {genero}": max_playtime_user_id,
        "Horas jugadas": playtime_by_year
    }



@app.get('/best_developer_year')
def best_developer_year(año: int):
    # Convertir 'release_date' a tipo fecha
    output_steam_games['release_date'] = pd.to_datetime(output_steam_games['release_date'])

    # Filtrar juegos por el año dado
    juegos_anio_dado = output_steam_games[output_steam_games['release_date'].dt.year == año]

    # Obtener los juegos únicos del año dado
    juegos_unicos_anio_dado = juegos_anio_dado['item_id'].unique()

    # Contar la cantidad de juegos recomendados por desarrollador para cada año
    desarrolladores_por_anio = {}
    for juego_id in juegos_unicos_anio_dado:
        # Filtrar revisiones para el juego actual y contar recomendaciones positivas
        revisiones_juego = user_reviews[user_reviews['item_id'] == juego_id]
        recomendaciones_positivas = revisiones_juego[(revisiones_juego['recommend'] == True) & (revisiones_juego['sentiment_analysis'] > 0)]
        desarrollador = juegos_anio_dado[juegos_anio_dado['item_id'] == juego_id]['developer'].iloc[0]

        # Actualizar el recuento de recomendaciones para el desarrollador
        if desarrollador in desarrolladores_por_anio:
            desarrolladores_por_anio[desarrollador] += len(recomendaciones_positivas)
        else:
            desarrolladores_por_anio[desarrollador] = len(recomendaciones_positivas)

    # Obtener el top 3 de desarrolladores con más juegos recomendados para el año dado
    top_desarrolladores = sorted(desarrolladores_por_anio.items(), key=lambda x: x[1], reverse=True)[:3]

    # Formatear los resultados en el formato requerido
    resultados = [{"Puesto {}: {}".format(idx+1, desarrollador) : juegos_recomendados} for idx, (desarrollador, juegos_recomendados) in enumerate(top_desarrolladores)]

    return resultados



@app.get('/developer_reviews_analysis')
def developer_reviews_analysis(desarrolladora: str):
    # Filtrar los juegos por el desarrollador dado
    juegos_desarrolladora = output_steam_games[output_steam_games['developer'] == desarrolladora]

    # Obtener los item_ids asociados al desarrollador
    item_ids_desarrolladora = juegos_desarrolladora['item_id']

    # Filtrar revisiones por los item_ids del desarrollador
    revisiones_desarrolladora = user_reviews[user_reviews['item_id'].isin(item_ids_desarrolladora)]

    # Contar revisiones con análisis de sentimiento negativo y positivo
    revisiones_negativas = len(revisiones_desarrolladora[revisiones_desarrolladora['sentiment_analysis'] == 0])
    revisiones_positivas = len(revisiones_desarrolladora[revisiones_desarrolladora['sentiment_analysis'] == 2])

    # Retornar los resultados
    return {desarrolladora: {'Negative': revisiones_negativas, 'Positive': revisiones_positivas}}


@app.get('/recomendacion_juego/{juego_id}')
def recomendacion_juego(juego_id: int):
    if juego_id not in steam_games['item_id'].unique():
        raise HTTPException(status_code=404, detail="Juego no encontrado")
    
    recomendaciones = get_recommendations(juego_id)
    
    # Filtrar los índices de los juegos recomendados para eliminar los NaN
    recomendaciones_filtradas = [idx for idx in recomendaciones if not pd.isnull(steam_games.iloc[idx]['title'])]
    
    titulos_recomendados = [steam_games.iloc[idx]['title'] for idx in recomendaciones_filtradas]
    
    return {
        "juego_id": juego_id,
        "recomendaciones": titulos_recomendados
    }





def get_recommendations(item_id, k=5):
    # Encontrar el índice correspondiente al juego_id proporcionado
    juego_idx = steam_games[steam_games['item_id'] == item_id].index
    if len(juego_idx) == 0:
        return ["No hay juegos recomendados"]  # Si no se encuentra el juego, devuelve un mensaje indicando que no hay juegos recomendados
    else:
        juego_idx = juego_idx[0]
        # Encontrar los índices de los vecinos más cercanos
        distances, indices = model.kneighbors(caracteristicas[juego_idx], n_neighbors=k+1)
        # Excluir el propio juego de las recomendaciones
        indices = indices[:, 1:]
        if len(indices) == 0:
            return ["No hay juegos recomendados"]  # Si no se encuentran juegos similares, devuelve un mensaje indicando que no hay juegos recomendados
        else:
            # Obtener los índices de los juegos recomendados
            return indices.flatten().tolist()

# esto fue añadido 11/07/25 para poder cargarlo a render
if __name__ == "__main__":
    import uvicorn, os
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Render sete­ará PORT
        reload=False
    )
