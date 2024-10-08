# World Cup Data Analysis

## Resumen

Este repositorio contiene un conjunto de scripts para el análisis y la predicción de los resultados de los Mundiales de la FIFA. Utilizando datos históricos y técnicas de modelado, el objetivo es limpiar, analizar y predecir resultados de partidos de la Copa del Mundo. Los datos son extraídos y procesados desde varias fuentes, incluyendo Wikipedia y scraping web.

## Objetivo

El objetivo principal es proporcionar un análisis detallado de los partidos de la Copa del Mundo a lo largo de los años y realizar predicciones sobre eventos futuros utilizando modelos estadísticos. El proceso incluye la recolección de datos, limpieza, análisis y la generación de predicciones para el Mundial de 2022.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para la implementación de los scripts.
- **Pandas**: Para la manipulación y análisis de datos.
- **NumPy**: Para operaciones matemáticas y estadísticas.
- **Matplotlib**: Para la visualización de datos (no utilizado directamente en los scripts proporcionados).
- **Selenium**: Para el web scraping de datos históricos.
- **BeautifulSoup**: Para el web scraping de datos históricos.
- **Requests**: Para realizar peticiones HTTP y obtener datos de páginas web.
- **Scipy**: Para el modelado estadístico y la predicción de resultados utilizando el modelo de Poisson.

## Proceso

1. **Extracción de Datos**:
   - Se utilizan scripts de web scraping (`worldcups_1930-2018.py` y `worldcup_1990.py`) para obtener datos de partidos de Mundiales desde Wikipedia.
   - Se realiza scraping de tablas específicas para el Mundial de 2022 utilizando `prediction_worldcup2022.py`.

2. **Limpieza y Procesamiento**:
   - Los datos son limpiados y procesados para eliminar duplicados, valores nulos y formatear las columnas correctamente (`analissar.py`).
   - Se generan archivos CSV con los datos limpios (`df_clean_worldcups.csv`).

3. **Análisis y Predicción**:
   - Se analiza el rendimiento de los equipos utilizando un modelo estadístico basado en el modelo de Poisson (`prediction.py`).
   - Se predicen los resultados de los partidos y se actualizan las tablas de fases del Mundial de 2022.

4. **Resultados**
   - El análisis proporciona una predicción de los resultados de los partidos de la Copa del Mundo 2022, actualizando los equipos avanzados a las etapas siguientes (octavos, cuartos, semifinales, final).

## Conclusión:

Este proyecto demuestra la capacidad de combinar técnicas de scraping, análisis de datos y modelado estadístico para obtener insights significativos sobre el desempeño en los torneos de la Copa del Mundo. Los resultados permiten entender mejor el rendimiento de los equipos y ofrecen predicciones basadas en datos históricos.

## Archivos y Scripts

- **`worldcups_1930-2018.py`**: Script para extraer datos históricos de Mundiales desde Wikipedia.
- **`worldcup_1990.py`**: Script para extraer datos del Mundial de 1990 utilizando Selenium.
- **`analissar.py`**: Script para limpiar y procesar los datos obtenidos.
- **`prediction_worldcup2022.py`**: Script para extraer datos de la Copa del Mundo 2022 y crear un diccionario de equipos.
- **`prediction.py`**: Script para realizar predicciones de partidos utilizando el modelo de Poisson.
