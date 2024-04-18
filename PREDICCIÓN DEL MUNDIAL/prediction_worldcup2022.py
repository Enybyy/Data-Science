import pandas as pd
import pickle

# INDICAR URL
url = 'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
# LEER URL
all_tables = pd.read_html(url)

"""
# Configuración para mostrar todas las columnas y alinear el texto a la izquierda
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

# CONTAR CUANTAS TABLAS EXISTEN EN LA WEB
print(f"EXISTEN: {len(all_tables)} tablas.")

# ITERAR SOBRE LAS TABLAS E IMPRIMIR TITULOS, PARA OBTENER LAS TABLAS QUE CONTIENEN LOS GRUPOS DE CADA EQUIPO
for i, table in enumerate(all_tables):
    # Obtener el título de la tabla (nombre de columnas)
    title = table.columns.tolist()
    print(f"Título de la tabla {i}: {title}")
"""

# DICCIONARIO DE LOS GRUPOS 'A' to 'H'
dict_groups = {}
# ITERAR SIMULTANEAMENTE DOS SECUENCIAS
for i, letra in zip(range(12, 62, 7), range(65, 73)):
    df = all_tables[i]
    df.drop(columns={'Qualification'}, inplace=True)
    df.rename(columns={'Teamvte': 'Team'}, inplace=True)
    # <-- CONVIERTE NUMERO A CARACTER 'Alt + {num}'
    dict_groups[f'Group {chr(letra)}'] = df
    # print(df.to_markdown(index=False), "\n")

print(dict_groups['Group A'].to_markdown(index=False), "\n")
for group_key in dict_groups:
    dict_groups[group_key]['Pts'] = dict_groups[group_key]['Pts'].astype(float)

# CAMBIAMOS TIPO DE DATO PARA EVITAR PROBLEMAS FUTUROS
for group_key in dict_groups:
    print(f"Tipos de datos para el grupo {group_key}:")
    print(dict_groups[group_key].dtypes)
    print()
# IMPORTAR DICCIONARIO
with open('dict_groups', 'wb')as ouput:
    pickle.dump(dict_groups, ouput)

print(dict_groups)
