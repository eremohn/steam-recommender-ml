from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Cargar los datos
user_reviews = pd.read_parquet('user_reviews.parquet')
output_steam_games = pd.read_parquet('output_steam_games.parquet')
australian_users_items = pd.read_parquet('australian_users_items.parquet')

@app.get('/')
def message():
    return "API de desarrolladores de juegos"

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
    user_items = user_items_df[user_items_df['user_id'] == user_id]
    
    # Calcular el dinero gastado por el usuario
    money_spent = user_items['item_id'].apply(lambda x: steam_games_df.loc[steam_games_df['item_id'] == x, 'price'].sum()).sum()
    
    # Calcular el porcentaje de recomendación promedio por usuario
    recommendation_percentage = user_reviews_df[user_reviews_df['user_id'] == user_id]['recommend'].mean() * 100
    
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
    # Eliminar filas con valores NaN en la columna 'genres'
    output_steam_games_cleaned = output_steam_games.dropna(subset=['genres'])
    
    # Filtrar los juegos por el género dado
    juegos_genero = output_steam_games_cleaned[output_steam_games_cleaned['genres'].str.contains(genero)]
    
    # Unir los DataFrames para obtener las horas jugadas por usuario
    horas_jugadas_por_usuario = pd.merge(juegos_genero, australian_users_items, on='item_id')
    
    # Sumar las horas jugadas por usuario
    horas_por_usuario = horas_jugadas_por_usuario.groupby('user_id')['playtime_forever'].sum().reset_index()
    
    # Obtener el usuario con más horas jugadas
    usuario_mas_horas = horas_por_usuario.loc[horas_por_usuario['playtime_forever'].idxmax()]
    
    # Calcular la acumulación de horas jugadas por año de lanzamiento
    horas_por_anio = juegos_genero.groupby('release_date')['playtime_forever'].sum().reset_index().to_dict('records')
    
    # Retornar los resultados
    return {
        "Usuario con más horas jugadas para " + genero: usuario_mas_horas['user_id'],
        "Horas jugadas": horas_por_anio
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

