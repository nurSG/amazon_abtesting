import pandas as pd

def minus(df):
  """
  Convierte en minúsculas todos los valores de las columnas categóricas de un DataFrame

  Parameters:
  df(pd.DataFrame): Dataframe que contiene las columnas a procesar

  Returns:
  None
  
  """
  for col in df.select_dtypes(include='O').columns:
    df[col]=df[col].str.lower()


def espacio(df):
  """
  Reemplaza esapcios por guines bajos en columnas especificadas del DataFrame

  Parameters:
  df(pd.DataFrame): Dataframe que contiene las columnas a procesar

  Returns:
  None
  
  """
  for col in df.select_dtypes(include='O').columns:
    df[col] = df[col].str.replace(" ","_")


def coma_float(df):
  """
  Reemplaza comas por puntos en columnas especificadas del DataFrame

  Parameters:
  df(pd.DataFrame): Dataframe que contiene las columnas a procesar
  lista_col(list of str): lista con los nombres de las columnas

  Returns:
  None
  
  """
  for col in df.select_dtypes(include='O').columns:
    df[col]=df[col].str.replace(",",".")
    try:
      df[col]=df[col].astype('float')
    except:
      pass