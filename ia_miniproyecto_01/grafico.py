import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ia_miniproyecto_01/datos.csv', encoding='utf-8-sig')
plt.figure()
plt.bar(df['nombre'], df['score'])
plt.title('Score por persona')
plt.ylabel('Score')
plt.savefig('ia_miniproyecto_01/grafico_scores.png', bbox_inches='tight')
print('ok:grafico_scores.png')
