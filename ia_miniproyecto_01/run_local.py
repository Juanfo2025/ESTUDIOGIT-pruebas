import os
import pandas as pd
from matplotlib import pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, 'datos.csv')
OUT_CSV = os.path.join(BASE, 'resumen.csv')
OUT_IMG = os.path.join(BASE, 'grafico_scores.png')

if not os.path.exists(CSV):
    with open(CSV, 'w', encoding='utf-8') as f:
        f.write('nombre,edad,score\\nAna,23,80\\nLuis,34,90\\nSofía,29,75\\n')

df = pd.read_csv(CSV, encoding='utf-8-sig')
print('filas:', len(df))
print('columnas:', df.shape[1])
print('promedio_score:', round(df['score'].mean(), 2))

df[['nombre','score']].to_csv(OUT_CSV, index=False, encoding='utf-8')
plt.figure()
plt.bar(df['nombre'], df['score'])
plt.title('Score por persona')
plt.ylabel('Score')
plt.savefig(OUT_IMG, bbox_inches='tight')
print('ok: resumen y gráfico listos')
