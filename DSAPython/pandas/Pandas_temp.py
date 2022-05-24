########################################################
#
#       ANÁLISE DAS TEMPERATURAS EM APROXIMADAMENTE 850
#       CIDADES BRASILEIRAS
#
########################################################

import pandas as pd
import matplotlib.pyplot as plt
import glob
import os


docs = glob.glob('C:\\Users\\adria\\OneDrive\\Documentos\\DSAPython\\openpyxl_lib\\files_xls\\*xlsx', recursive = True)

size = len(docs)

print(size)

sample = 10
df = pd.DataFrame()
df_cons = pd.DataFrame()
for doc in docs:
    df_doc = pd.read_excel(doc)
    df = [df,df_doc]
    df = pd.concat(df)
    print(doc)
    print(len(df))
    sample = sample - 1
    if sample <= 0:
        break

print("Remove columns no utility!!!\n")
df.drop(['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)',
         'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)',
         'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)',
         'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
         'RADIACAO GLOBAL (Kj/m²)',
         'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)',
         'TEMPERATURA DO PONTO DE ORVALHO (°C)',
         'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)',
         'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)',
         'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)',
         'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)',
         'UMIDADE RELATIVA DO AR, HORARIA (%)',
         'VENTO, DIREÇÃO HORARIA (gr) (° (gr))',
         'VENTO, RAJADA MAXIMA (m/s)',
         'VENTO, VELOCIDADE HORARIA (m/s)'], axis = 1, inplace = True)

print("Rename columns")
df2 = df.rename(columns = {'Hora UTC' : 'hora_utc',
                   'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)' : 'temp_max',
                   'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)' : 'temp_min',
                   'REGIAO:' : 'regiao',
                   'UF:' : 'uf',
                   'ESTACAO:' : 'estacao',
                   'CODIGO (WMO):' : 'codigo_wmo',
                   'LATITUDE:' : 'latitude',
                   'LONGITUDE:' : 'longitude',
                   'ALTITUDE:' : 'altitude',
                   'DATA DE FUNDACAO:' : 'dt_fundacao'})
print(df2.head(n=10))

#This function is similar select distintic from sql
df2.drop_duplicates(subset = ['hora_utc'])
    















    
