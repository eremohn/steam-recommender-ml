import json
import pandas as pd

# función para cargar y corregir cada línea del archivo JSON original
def cargar_y_corregir_linea(linea):
    # Cambiar comillas simples por comillas dobles
    linea_corregida = linea.replace("'", '"')
    return json.loads(linea_corregida)

# lista para almacenar los datos desanidados
data_list = []

# leer el archivo JSON original, corregir y procesar cada línea
with open('australian_users_items.json', 'r', encoding='utf-8') as archivo_json:
    for linea in archivo_json:
        try:
            entrada = cargar_y_corregir_linea(linea)
            user_id = entrada['user_id']
            items_count = entrada['items_count']
            steam_id = entrada['steam_id']
            user_url = entrada['user_url']
            # iteracion sobre cada item
            for item in entrada['items']:  # Aquí accedemos a la clave 'items' del diccionario 'entrada'
                item_dict = {
                    'user_id': user_id,
                    'items_count': items_count,
                    'steam_id': steam_id,
                    'user_url': user_url,
                    'item_id': item['item_id'],  # No necesitas .get() aquí, ya que sabemos que 'item_id' está presente
                    'item_name': item['item_name'],  # Tampoco necesitas .get() aquí
                    'playtime_forever': item['playtime_forever'],  # Tampoco necesitas .get() aquí
                    'playtime_2weeks': item['playtime_2weeks']  # Tampoco necesitas .get() aquí
                }
                data_list.append(item_dict)  # Agregamos el diccionario 'item_dict' a la lista 'data_list'
        except json.JSONDecodeError as e:
            None

# crear el DataFrame
df = pd.DataFrame(data_list)

# guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('australian_users_items.csv', index=False)

# guardar el DataFrame modificado en un nuevo archivo Parquet
df.to_parquet('australian_users_items.parquet', index=False)

print("El archivo 'australian_users_items.csv' y 'australian_users_items.parquet' han sido creados con éxito.")
