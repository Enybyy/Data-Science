import pandas as pd

df_worldcup_history = pd.read_csv('Database/worldcup_history.csv')
df_worldcup_1990 = pd.read_csv('Database/worldcup_1990.csv')
df_worldcup_2022 = pd.read_csv('Database/worldcup_2022.csv')

# VERIFIVAR VALROES NULOS
# null_values_history = df_worldcup_1990.isnull().sum()
# print("Valores nulos en df_worldcup_history:")
# print(null_values_history)

# QUITAR ESPACIOS EN BLANCO '.strip'
df_worldcup_history['local_teams'] = df_worldcup_history['local_teams'].str.strip()
df_worldcup_history['away_teams'] = df_worldcup_history['away_teams'].str.strip()
df_worldcup_1990['local_teams'] = df_worldcup_1990['local_teams'].str.strip()
df_worldcup_1990['away_teams'] = df_worldcup_1990['away_teams'].str.strip()
df_worldcup_2022['local_teams'] = df_worldcup_2022['local_teams'].str.strip()
df_worldcup_2022['away_teams'] = df_worldcup_2022['away_teams'].str.strip()

# print(df_worldcup_1990[df_worldcup_1990['local_teams'].isnull()])
pd.set_option('display.max_rows', None)
# CONCATENAR DF
df_worldcup_history = pd.concat(
    [df_worldcup_1990, df_worldcup_history])
# ELIMINAR DUPLICADOS
df_worldcup_history.drop_duplicates(inplace=True)
# ORDENAR DF por 'year'
df_worldcup_history.sort_values('year', ignore_index=True, inplace=True)
# ELIMINAR TODAS LAS FILAS QUE CONTENGAN 'w/o'
df_worldcup_history.drop(
    df_worldcup_history[df_worldcup_history['score'].str.contains('w/o')].index, inplace=True)

# FILTRAR FILAS QUE CONTENGAS LETRAS EN LA COLUMNA 'score'
# filter1 = df_worldcup_history[df_worldcup_history['score'].str.contains(
#     '[a-zA-Z]')]
# FILTRAR FILAS QUE CONTENGAS LETRAS EN LA COLUMNA 'score'
# filter2 = df_worldcup_history[df_worldcup_history['score'].str.contains('[^\d–]')]

# REEMPLAZAMOS LOS CHAR QUE NO SEAN NUMEROS O '–' GUIÓN LARGO, POR '' NADA.
df_worldcup_history['score'] = df_worldcup_history['score'].str.replace(
    r'[^\d–]', '', regex=True)
# LIMPIAMOS DATOS
df_worldcup_history['local_teams'] = df_worldcup_history['local_teams'].str.strip()
df_worldcup_history['score'] = df_worldcup_history['score'].str.strip()
df_worldcup_history['away_teams'] = df_worldcup_history['away_teams'].str.strip()

# DIVIDIR COLUMNA 'score' EN DOS COLUMNAS USANDO '–' COMO DELIMITADOR
df_worldcup_history[['Local_Goals', 'Away_Goals']
                    ] = df_worldcup_history['score'].str.split('–', expand=True)

df_worldcup_history.drop('score', axis=1, inplace=True)
df_worldcup_history.rename(
    columns={'local_teams': 'Local_Team', 'away_teams': 'Away_Team', 'year': 'Year'}, inplace=True)

df_worldcup_history = df_worldcup_history.astype(
    {'Local_Goals': int, 'Away_Goals': int})

df_worldcup_history.to_csv('Database/df_clean_worldcups.csv', index=False)

print(df_worldcup_history.dtypes)
print(df_worldcup_history.head().to_markdown())
