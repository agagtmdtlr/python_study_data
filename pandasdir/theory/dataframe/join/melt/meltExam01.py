import pandas as pd
from pandas import DataFrame

siljuk = pd.read_csv('siljuk.csv')
print(siljuk)

siljuk_long = pd.melt(siljuk, id_vars=['religion'])
print(siljuk_long)
print('-'*30)

siljuk_long = pd.melt(siljuk, id_vars=['religion'],
                      var_name='income', value_name='count')
print(siljuk_long)
print('-'*30)

siljuk_long = pd.melt(siljuk, id_vars=['religion'],
                      var_name='income', value_name='count')
print(siljuk_long)
print('-'*30)

siljuk_long = pd.melt(siljuk, id_vars=['religion'],
                      value_vars=['$1사분기','$2사분기'],
                      var_name='income', value_name='count')
print(siljuk_long)
print('-'*30)

newsiljuk = pd.read_csv('siljuk2.csv')
newsiljuk_long = pd.melt(newsiljuk, id_vars=['religion','dong'],
                         var_name='income', value_name='count')
print('siljuk2')
print(newsiljuk_long)
print('-'*40)
