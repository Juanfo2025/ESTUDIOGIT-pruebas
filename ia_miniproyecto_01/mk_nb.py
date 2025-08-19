import nbformat as nbf
data_path = r'C:/Users/balla/OneDrive/Desktop/ESTUDIOGIT/ia_miniproyecto_01/datos.csv'
out_img = r''
out_csv = r''

nb = nbf.v4.new_notebook()
cells = []
cells.append(nbf.v4.new_markdown_cell('# Mini-proyecto IA — mp01 (abs paths)'))
cells.append(nbf.v4.new_code_cell(
    "import pandas as pd\n"
    f"df = pd.read_csv(r'{DATA_PATH}', encoding='utf-8-sig')\n"
    "print('filas:', len(df))\n"
    "print('columnas:', df.shape[1])\n"
    "print('promedio_score:', round(df['score'].mean(), 2))"
))
cells.append(nbf.v4.new_code_cell(
    "import matplotlib\n"
    "matplotlib.use('Agg')\n"
    "import matplotlib.pyplot as plt\n"
    f"df = pd.read_csv(r'{DATA_PATH}', encoding='utf-8-sig')\n"
    "plt.figure()\n"
    "plt.bar(df['nombre'], df['score'])\n"
    "plt.title('Score por persona')\n"
    "plt.ylabel('Score')\n"
    f"plt.savefig(r'{OUT_IMG}', bbox_inches='tight')\n"
    "print('ok:grafico_scores.png')"
))
cells.append(nbf.v4.new_code_cell(
    "import pandas as pd\n"
    f"df = pd.read_csv(r'{DATA_PATH}', encoding='utf-8-sig')\n"
    f"df[['nombre','score']].to_csv(r'{OUT_CSV}', index=False, encoding='utf-8')\n"
    "print('ok:resumen.csv')"
))
nb['cells'] = cells
with open('ia_miniproyecto_01/mp01.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print('ok:notebook')
