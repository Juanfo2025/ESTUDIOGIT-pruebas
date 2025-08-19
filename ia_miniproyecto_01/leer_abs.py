import os, pandas as pd
from matplotlib import pyplot as plt

CSV = r'C:/Users/balla/OneDrive/Desktop/ESTUDIOGIT/ia_miniproyecto_01/datos.csv'
OUT_CSV = r''
OUT_IMG  = r''

assert os.path.exists(CSV), f'No existe CSV: {CSV}'
df = pd.read_csv(CSV, encoding='utf-8-sig')

print('filas:', len(df))
print('columnas:', df.shape[1])
print('promedio_score:', round(df['score'].mean(), 2))

# Guardar resumen y gráfico
df[['nombre','score']].to_csv(OUT_CSV, index=False, encoding='utf-8')
plt.figure()
plt.bar(df['nombre'], df['score'])
plt.title('Score por persona')
plt.ylabel('Score')
plt.savefig(OUT_IMG, bbox_inches='tight')
print('ok: resumen.csv y grafico_scores.png')
