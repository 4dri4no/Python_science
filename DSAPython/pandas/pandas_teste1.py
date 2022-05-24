import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

notas = pd.Series([2,3,4,5,6])
nome = pd.Series(['Adriano', 'Junio', 'Denis', 'Julia', 'Nicole'])

data = {
    'animal': ['cachorro', 'gato', 'coruja'],
    'cidade': ['Rio de janeiro', 'Sao paulo','Bahia', 'Salvador']}

df = pd.DataFrame(data, columns = ['animal'])


'''
Ler quivos em csv

x = pd.read_csv('C:\\Users\\adria\\OneDrive\\Documentos\\DSAPython\\pandas\\xls\\Pasta1.csv',
            encoding='ISO-8859-1')
print(x)
'''


rj = pd.read_csv('C:\\Users\\adria\\OneDrive\\Documentos\\DSAPython\\pandas\\xls\\Rio_de_janeiro.csv',
                 encoding='ISO-8859-1')
print(rj)




