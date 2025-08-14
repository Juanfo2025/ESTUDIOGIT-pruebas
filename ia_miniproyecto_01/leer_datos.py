import pandas as pd
df = pd.read_csv('ia_miniproyecto_01/datos.csv', encoding='utf-8-sig')
print('filas:', len(df))
print('columnas:', df.shape[1])
print('promedio_score:', round(df['score'].mean(), 2))
