# EXTRAER DATOS CON WEB SCRAPING
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# RUTA DEL ARCHIVO CHROMEDRIVER
path = 'C:/chromedriver/chromedriver-win64/chromedriver.exe'

# INICIALIZAR SERVICIO DE GOOGLE CHROME
service = Service(executable_path=path)

# INIACIALIZAR GOOGLE CHROME
driver = webdriver.Chrome(service=service)

# URL
web = 'https://en.wikipedia.org/wiki/1990_FIFA_World_Cup'

# INICIAR PAGINA WEB
driver.get(web)
time.sleep(4)

matches = driver.find_elements(
    by='xpath', value='//tr[@style="font-size:90%"] | //tr[@itemprop="name"]')

# LISTAS
fhome = []
fscore = []
faway = []

# ITERAR SOBRE CADA ELEMNTO
for match in matches:
    fhome.append(match.find_element(
        by='xpath', value='./td[1] | ./th[1]').text.strip())
    fscore.append(match.find_element(
        by='xpath', value='./td[2] | ./th[2]').text.strip())
    faway.append(match.find_element(
        by='xpath', value='./td[3] | ./th[3]').text.strip())

dict_football = {'local_teams': fhome,
                 'score': fscore, 'away_teams': faway}
# CONVERTIR A DF
df_worldcup1990 = pd.DataFrame(dict_football)
# AGREGAR EL AÑO
df_worldcup1990['year'] = 1990
time.sleep(1)

# GUARDAR DF EN DOCUMENTO '.cvs"
df_worldcup1990.to_csv('Database/worldcup_1990.csv', index=False)
# print(df_worldcup1990)

# SALIR
driver.quit()
