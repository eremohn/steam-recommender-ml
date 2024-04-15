import json
import pandas as pd
import re
from textblob import TextBlob  # asegurarse de tener instalada la biblioteca TextBlob previamente

# funcion para corregir y cargar cada linea del archivo 'australian_user_reviews.json' original
def cargar_y_corregir_linea(linea):
    # reemplaza las comillas simples con dobles y corrige valores booleanos
    linea_corregida = linea.replace("'", '"').replace('True', 'true').replace('False', 'false')
    return json.loads(linea_corregida)

# lista para almacenar los datos desanidados
data_list = []

# exprecion regular para extraer números de la columna 'funny'
numero_regex = re.compile(r'\d+')

# lee el archivo 'australian_user_reviews.json' original, corrige y procesa cada línea
with open('australian_user_reviews.json', 'r', encoding='utf-8') as archivo_json:
    for linea in archivo_json:
        try:
            entrada = cargar_y_corregir_linea(linea)
            user_id = entrada['user_id']
            user_url = entrada['user_url']
            # iteracion sobre cada reseña
            for reseña in entrada['reviews']:
                # estrae el numero de la columna 'funny'
                funny_valor = re.search(numero_regex, reseña.get('funny', ''))
                if funny_valor:
                    funny = int(funny_valor.group())
                else:
                    funny = None
                
                # elimina 'Posted' de la columna 'posted'
                posted = reseña.get('posted', '').replace('Posted ', '', 1)

                reseña_dict = {
                    'user_id': user_id,
                    'user_url': user_url,
                    'funny': funny,
                    'posted': posted,
                    'item_id': int(reseña.get('item_id', '')),  # convierte a entero
                    'helpful': reseña.get('helpful', ''),
                    'recommend': reseña.get('recommend', ''),
                    'review': reseña.get('review', '')  # mantiene el texto original de la review
                }
                data_list.append(reseña_dict)
        except json.JSONDecodeError as e:
            None

# crea el DataFrame
df = pd.DataFrame(data_list)

# elimina la columna 'last_edited' 
if 'last_edited' in df.columns:
    df.drop(columns=['last_edited'], inplace=True) 

# funcion para analizar el sentimiento de la reseña
def analyze_sentiment(review):
    if pd.isna(review) or not isinstance(review, str):
        return 1  # Sentimiento neutral para reseñas faltantes o no legibles
    else:
        # se emplea TextBlob para calcular la polaridad del sentimiento
        polarity = TextBlob(review).sentiment.polarity
        if polarity < 0:
            return 0  # sentimiento negativo
        elif polarity == 0:
            return 1  # sentimiento neutral
        else:
            return 2  # sentimiento positivo

# aplicacion de la funcion analyze_sentiment a cada reseña y crea la nueva columna 'sentiment_analysis'
df['sentiment_analysis'] = df['review'].apply(analyze_sentiment)

# Convertir la columna 'posted' a tipo datetime
df['posted'] = pd.to_datetime(df['posted'], errors='coerce')

# elimina la columna original 'review'
df.drop(columns=['review'], inplace=True)

# Convertir la columna 'posted' a tipo datetime
df['posted'] = pd.to_datetime(df['posted'], errors='coerce')

# guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv('user_reviews.csv', index=False)

# guarda el DataFrame modificado en un nuevo archivo Parquet
df.to_parquet('user_reviews.parquet', index=False)

print("El analisis de sentimiento ha sido aplicado y guardado en 'user_reviews.csv' y 'user_reviews.parquet'.")
