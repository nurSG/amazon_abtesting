# Vamos a generar una función que contenga todo lo que hacemos a contuniación porque es un proceso común de limpieza. De este modo la próxima vez podremos llamar a la función con otra base de datos y que le aplique los mismo métodos y herramientas.

# Tratamiento de datos
import pandas as pd

def eda_preliminar(df):
  """
  Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

  Este análisis incluye:
  - Muestra aleatoria de 5 filas del Dataframe
  - Información general de DataFrame(tipo de datos, nulos, etc.)
  - Porcentaje de valores nulos por columna
  - Conteo de filas dulpicadas
  - Distribución de valores para columnas categóricas

  Parameters:
  df (pd.DataFrame) : Dataframe a analizar.

  Returns:
  None 
  
  """
  display(df.sample(5)) # para ver un data frame es mejor diplay, con print sale en otro formato

  print('-----------------------------')
  
  print('DIMENSIONES')
  print(f"Mi data frame tiene {df.shape[0]} filas y {df.shape[1]} columnas")

  print('-----------------------------')

  print('INFO')
  display(df.info())
  
  print('-----------------------------')

  print('NULOS')
  display(df.isnull().sum()/ df.shape[0] * 100)

  print('-----------------------------')

  print('DUPLICADOS')
  print(f"Tenemos un total de {df.duplicated().sum()} duplicados")

  print('-----------------------------')

  print('FRECUENCIA CATEGORICAS')
  for col in df.select_dtypes(include="O").columns:
    print(col.upper())
    print(df[col].value_counts())
    print('-----------')

