def calculo_ouliers(df,cols):
  for col in cols:
    q_75 = df[col].quantile(0.75)
    q_25 = df[col].quantile(0.25)
    rango_itq = q_75 - q_25
    inferior = q_25 - (rango_itq*1.5)
    superior = q_75 + (rango_itq*1.5)
    
    outliers = df[(df[col] < inferior)   |  (df[col] > superior)]
    num_outliers = len(outliers)

    por_outliers= num_outliers/df.shape[0]*100
    print(f' En la columna {col.upper()}, hay un total de {num_outliers} outliers, lo que representa un {por_outliers} %')


def imputar_iterative(dataframe, lista_columnas):
  iter_imputer = IterativeImputer( max_iter= 50,
                                  random_state= 42)
  data_imputed = iter_imputer.fit_transform(dataframe[lista_columnas])
  new_col = [col + "_iterative" for col in lista_columnas]
  dataframe[new_col] = data_imputed
  return dataframe



def imputar_knn(dataframe, lista_columnas):
  knn_imputer = KNNImputer(n_neighbors= 5)
  data_imputed = knn_imputer.fit_transform(dataframe[lista_columnas])
  new_col = [col + "_knn" for col in lista_columnas]
  dataframe[new_col] = data_imputed
  return dataframe