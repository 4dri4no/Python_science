#===================================================================
#
#               ANÁLISE COM PANDAS
#
#===================================================================

#Criado por Wes McKinney, Pandas surgiu em 2008 com recursos flexíveis para manipulação de planilhas e de banco de dados relacionais
#o nome Pandas se dá pelo derivado das palavras panel data (Dados em painéis)

import pandas as pd
import matplotlib.pyplot as plt
import glob

pd.get_option("display.max_columns")

#Carrega um arquivo de extensão .xlsx em forma de DataFrame
df = pd.read_excel('C:\\Users\\adria\\OneDrive\\Documentos\\DSAPython\\openpyxl_lib\\files_xls\\INMET_SE_RJ_A607_CAMPOS DOS GOYTACAZES_01-01-2021.xlsx')
print(type(df))

xlsx_files = glob.glob('C:\\Users\\adria\\OneDrive\\Documentos\\DSAPython\\openpyxl_lib\\files_xls\\*.xlsx', recursive = True)
contador = 10
dfxgroup = pd.DataFrame()
for file in xlsx_files:
    print(file)
    print('Size :' + str(len(file)) + '\n' + 'Tipo :' + str(type(file)))
    contador = contador - 1
    dfx = pd.read_excel(file)
    dfxgroup = pd.concat([dfxgroup,dfx]) 
    if contador == 0:
        print('FINISHED!!!!!!!!!!!!!!!!!!')
        break


#-----------------------------
#Exibe às primeiras 10 linhas
##print(df.head(n=10))
#df = pd.read_excel('C:\\Users\\adria\\OneDrive\\Documentos\\DSAPython\\openpyxl_lib\\files_xls\\INMET_SE_RJ_A607_CAMPOS DOS GOYTACAZES_01-01-2021.xlsx',
#                   na_values = ['',''])

#Exibe as 10 últimas linhas
##print(df.tail(n=10))
#Obtem-se a quantidade de observação e colunas
##print(df.shape)
#Obtem-se informações a respeito do dataframe, como: Nome/tipo das variáveis, quantidade de observações de cada variável e memória
#utilizada
##print(df.info())
#Criando funções para tratamento de dados de uma série (pandas) ou variávis (estatística)
#Alterado o nome das colunas
#df.columns
#Index([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27], dtype = 'object')
#df.columns[]

#Resumo de ocorrências de campos com 'n/a', muito útil para tratativa dos dados que constam campos vazios. Interessante trabalhar
#essa função com o parâmetro na_values=['--','n/a','nada'] da função read_excel()
##df.isnull().sum()
#Para substituir valores nulos (n/a)
##df = df.fillna(value=0)
#ou
##df = df.fillna(method='ffill')

#Deleta todas as observações que apresentarem uma variável ou campo nulo
##df = df.dropna()

#Tratar apenas uma coluna
##df['Data'].head(n=5)
##type(df['Data'])
#Ploting Charts
##graf = df['Data'].value_counts().plot(kind='bar')
#graf.plot()
#plt.show()
#também pode ser assim:
##df['Data'].head(n=200).value_counts().plot(kind='bar').plot()
##plt.show()

#Vamos começar usufruindo do método map. Esse método apresenta um objetivo muito parecido ao do método apply. Entretanto,
#o apply pode ser aplicado em objetos do tipo Serie e do tipo DataFrame, enquanto o map somente em objetos Serie.
#df['valor_total'] = df['valor_total'].map(lambda x: str(x).replace('R$ ', ''))
#Veja que agora ao invés de passarmos o nome da função que criamos antes de aplicar um método de transformação, estamos
#utilizando o recurso denominado lambda que permite a criação de funções anônimas em Python. Essa nossa função substitui
#os caracteres formados pelo cifrão da moeda reais por nada. Podemos verificar o resultado, observando o primeiro elemento
#da nossa Serie:

#Para separar uma submatriz de outra matriz:
      #range obs. #range variávels/colunas
##df.loc[0:3, 'id':'valor']
#ou
##df.iloc[0:3,0:3]
#ou somente pelo nome das colunas com base na série
##df.loc[df['setor'] == 'informatica','valor_total']
#ou o valor total
##df.loc[df['setor'] == 'informatica','valor_total'].sum()
#Enfim...

#Resumo estatístico
##df.describe()


#------------------------------------------------------------------------
#O comando abaixo exibe todas as colunas do DataFrame
'''
df.columns
Index(['Data', 'Hora UTC', 'PRECIPITAÇÃO TOTAL, HORÁRIO (mm)',
       'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)',
       'PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)',
       'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
       'RADIACAO GLOBAL (Kj/m²)',
       'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)',
       'TEMPERATURA DO PONTO DE ORVALHO (°C)',
       'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)',
       'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)',
       'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)',
       'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)',
       'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)',
       'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)',
       'UMIDADE RELATIVA DO AR, HORARIA (%)',
       'VENTO, DIREÇÃO HORARIA (gr) (° (gr))', 'VENTO, RAJADA MAXIMA (m/s)',
       'VENTO, VELOCIDADE HORARIA (m/s)', 'REGIAO:', 'UF:', 'ESTACAO:',
       'CODIGO (WMO):', 'LATITUDE:', 'LONGITUDE:', 'ALTITUDE:',
       'DATA DE FUNDACAO:'],
      dtype='object')
'''
#Removendo colunas não consideradas na análise
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
       'VENTO, DIREÇÃO HORARIA (gr) (° (gr))', 'VENTO, RAJADA MAXIMA (m/s)',
       'VENTO, VELOCIDADE HORARIA (m/s)'],axis = 1, inplace=True)
#Reexibir os nomes das colunas para serem alterados
print(df.columns)
'''
Index(['Data', 'Hora UTC', 'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)',
       'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)', 'REGIAO:', 'UF:',
       'ESTACAO:', 'CODIGO (WMO):', 'LATITUDE:', 'LONGITUDE:', 'ALTITUDE:',
       'DATA DE FUNDACAO:'],
      dtype='object')
'''

df2 = df.rename(columns={'Hora UTC' : 'hora_utc',
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
#df.rename(index={0:'Hora_UTC'})

pd.get_option("display.max_columns")

pd.set_option('display.max_columns', None)

df4 = pd.DataFrame({'Date':df2['Data'],'temp_min':df2['temp_min']})

#df5 = df4.drop(df4.index[100:])
df5 = df4

df5['temp_min'] = df5['temp_min'].str.replace(',','.')

df5['temp_min'] = df5['temp_min'].astype(float)

df5.plot(kind='line', x = 'Date', y  = 'temp_min')
plt.show()

##Plot chart with two lines

ax = plt.gca()
df6 = pd.DataFrame({'Date':df2['Data'], 'temp_min':df2['temp_min'], 'temp_max':df2['temp_max']})
#df6 = df6.drop(df6.index[100:])
df6['temp_min'] = df6['temp_min'].str.replace(',','.')
df6['temp_min'] = df6['temp_min'].astype(float)
df6['temp_max'] = df6['temp_max'].str.replace(',','.')
df6['temp_max'] = df6['temp_max'].astype(float)

df6.plot(kind = 'line', x = 'Date', y = 'temp_min', ax = ax)
df6.plot(kind = 'line', x = 'Date', y = 'temp_max', color = 'red', ax = ax)

plt.show()

df2['longitude'] = df2['longitude'].str.replace(',','.')
df2['longitude'] = df2['longitude'].astype(float)
plt.scatter(df2['longitude'].values,
             df2['latitude'].values,
             s = 5 , c = 'blue',
             alpha = 0.5, zorder = 500)

plt.show()















