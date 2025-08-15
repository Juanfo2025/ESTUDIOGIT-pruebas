import os, pandas as pd, numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
RAW  = os.path.join(BASE, 'datos_mp02.csv')
OUTC = os.path.join(BASE, 'datos_mp02_limpio.csv')
OUTS = os.path.join(BASE, 'resumen_mp02.csv')

# Cargar (UTF-8 con BOM si hubiera)
df = pd.read_csv(RAW, encoding='utf-8-sig')

filas_antes = len(df)

# Normalizar texto
df['nombre'] = df['nombre'].astype(str).str.strip()

# Tipos numéricos
df['edad']  = pd.to_numeric(df['edad'], errors='coerce')
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# Reglas de limpieza:
# 1) eliminar filas sin nombre
df = df[df['nombre'].str.len() > 0]

# 2) imputar faltantes numéricos con mediana
for col in ['edad','score']:
    med = df[col].median()
    df[col] = df[col].fillna(med)

# 3) recortar outliers de score al rango [0,100]
df['score'] = df['score'].clip(0, 100)

# 4) quitar duplicados exactos
df = df.drop_duplicates()

filas_despues = len(df)

# Guardar resultados
df.to_csv(OUTC, index=False, encoding='utf-8')
pd.DataFrame([{
    'filas_antes': filas_antes,
    'filas_despues': filas_despues,
    'columnas': df.shape[1],
    'score_promedio': round(df['score'].mean(), 2)
}]).to_csv(OUTS, index=False, encoding='utf-8')

print('ok: mp02 limpio')
