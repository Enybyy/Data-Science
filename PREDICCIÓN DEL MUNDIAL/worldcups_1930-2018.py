# IMPORTAR LIBRERIAS
import requests
from bs4 import BeautifulSoup
import pandas as pd


def worldcup_history(year):
    # CONERTAR URL
    url = f"https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup"
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    # DATAFRAME
    fhome = []
    fscore = []
    faway = []

    # ITERAR SOBRE LOS EQUIPOS Y EXTRAER DATOS
    matches = soup.find_all('div', class_='footballbox')
    for match in matches:
        fhome.append(match.find('th', class_='fhome').text.strip())
        fscore.append(match.find('th', class_='fscore').text.strip())
        faway.append(match.find('th', class_='faway').text.strip())

    # DICCIONARIO
    dict_football = {'local_teams': fhome,
                     'score': fscore, 'away_teams': faway}
    df_football_worldcups = pd.DataFrame(dict_football)
    # AGREGAMOS EL AÑO 'year'
    df_football_worldcups['year'] = year
    return df_football_worldcups


# LISTA DE LOS MUNDIALES
years = ['1930', '1934', '1938', '1950', '1954', '1958', '1962', '1966', '1970', '1974',
         '1978', '1982', '1986', '1990', '1994', '1998', '2002', '2006', '2010', '2014', '2018']

# CREAMOS LISTA DE LOS MUNDIALES E ITERAMOS
dfs_worldcup_history = [worldcup_history(year) for year in years]
# CONCATENAR LOS LOS DF EN UNO SOLO
df_worldcup_history = pd.concat(dfs_worldcup_history)
# print(df_worldcup_history.to_markdown(index=False))

# GUARDAR DF COMO ARCHIVO '.csv'
df_worldcup_history.to_csv('Database/worldcup_history.csv', index=False)

# df_worldcup_history.to_csv('Database/worldcup_2022.csv', index=False)

# COMPROBAR SI LOS PARTIDOS SON CORRECTOS
# for year in years:
#     print(worldcup_history(year))
