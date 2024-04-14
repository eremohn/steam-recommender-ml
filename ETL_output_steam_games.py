import pandas as pd

# Lee el archivo JSON
df = pd.read_json('output_steam_games.json', lines=True)

# Elimina las filas vacías
df = df.dropna(how='all')

# Cambia el nombre de la columna 'id' a 'item_id'
df.rename(columns={'id': 'item_id'}, inplace=True)

# Función para convertir valores de 'price' a float o a 0 si no se puede convertir
def convert_to_float_or_zero(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0

# Aplica la función a la columna 'price'
df['price'] = df['price'].apply(convert_to_float_or_zero)

# Cambia los valores de la columna 'early_access' de acuerdo a la especificación
df['early_access'] = df['early_access'].replace({0.0: False, 1.0: True})

# Transforma los valores en formato 'yyyy-mm-dd' a fecha en la columna 'release_date'
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Reemplaza 'Soon..' por NaN en la columna 'release_date'
df['release_date'] = df['release_date'].replace('Soon..', pd.NaT)

# Guarda el DataFrame en un archivo CSV
df.to_csv('output_steam_games.csv', index=False)

# Guarda el DataFrame en un archivo Parquet
df.to_parquet('output_steam_games.parquet', index=False)
