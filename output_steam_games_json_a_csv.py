import pandas as pd 

# Lee el archivo JSON
df = pd.read_json('output_steam_games.json', lines=True)

# Elimina las filas vacías
df = df.dropna(how='all')

# Eliminar todo valor que sea string en la columna 'release_date'
df = df[pd.to_numeric(df['release_date'], errors='coerce').notna()]

# Transformar la columna 'release_date' a formato de fecha
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Transformar todos los valores faltantes en la columna 'price' a NaN
df['price'] = df['price'].replace('', pd.NA)

# Reemplazar todos los valores que contienen la palabra 'free' en la columna 'price' por 0
df['price'] = df['price'].replace('free', 0, regex=True)

# Reemplazar los puntos por comas en la columna 'price'
df['price'] = df['price'].str.replace('.', ',')

# Guarda el DataFrame en un archivo CSV
df.to_csv('output_steam_games.csv', index=False)

# Guarda el DataFrame en un archivo CSV
df.to_csv('output_steam_games.csv', index=False)
