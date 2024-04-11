import os
import csv
import json
import pandas as pd

# función para corregir y cargar cada línea del archivo 'user_reviews.json' original
def cargar_y_corregir_linea(linea):
    # reemplaza las comillas simples con dobles y corrige valores booleanos
    linea_corregida = linea.replace("'", '"').replace('True', 'true').replace('False', 'false')
    return json.loads(linea_corregida)

# función para limpiar la columna 'funny'
def clean_funny(funny):
    if pd.isna(funny):
        return ''
    else:
        # Si funny es un string, intenta extraer los números
        if isinstance(funny, str):
            funny = ''.join(filter(str.isdigit, funny))
            return funny
        else:
            return ''

# función para limpiar la columna 'posted'
def clean_posted(posted):
    if pd.isna(posted):
        return ''
    else:
        # Eliminar 'Posted' si está presente
        return posted.replace('Posted', '')

# nombre del archivo
file_name = 'user_reviews.csv'

# obteiene la ruta del directorio de trabajo actual
current_dir = os.getcwd()

# combina el directorio de trabajo actual con el nombre del archivo
file_path = os.path.join(current_dir, file_name)

# crea y abre un archivo 'user_reviews.csv' para escribir los datos
with open(file_path, 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    # escribe la fila de encabezado
    encabezado = ['user_id', 'user_url', 'funny', 'posted', 'last_edited', 'item_id', 'helpful', 'recommend', 'review']
    escritor_csv.writerow(encabezado)
    
    # lee el archivo 'user_reviews.json' original, corrige y procesa cada línea
    with open('australian_user_reviews.json', 'r', encoding='utf-8') as archivo_json:
        for linea in archivo_json:
            try:
                entrada = cargar_y_corregir_linea(linea)
                user_id = entrada['user_id']
                user_url = entrada['user_url']
                # iteracion sobre cada review
                for reseña in entrada['reviews']:
                    # aplicar las correcciones a 'funny' y 'posted'
                    funny = clean_funny(reseña.get('funny', ''))
                    posted = clean_posted(reseña.get('posted', ''))
                    
                    escritor_csv.writerow([
                        user_id,
                        user_url,
                        funny,
                        posted,
                        reseña.get('last_edited', ''),
                        reseña.get('item_id', ''),
                        reseña.get('helpful', ''),
                        reseña.get('recommend', ''),
                        reseña.get('review', '')  # asume que quieres mantener el texto original de la review
                    ])
            except json.JSONDecodeError as e:
                None

print("Los datos han sido convertidos y guardados en 'user_reviews.csv'.")
