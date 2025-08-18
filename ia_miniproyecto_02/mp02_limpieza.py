import pandas as pd
from pathlib import Path

# Rutas
mp02 = Path("ia_miniproyecto_02")
raw_path = mp02 / "datos_mp02.csv"
clean_path = mp02 / "datos_mp02_limpio.csv"
summary_path = mp02 / "resumen_mp02.csv"

# === Parte 1: leer ===
df = pd.read_csv(raw_path, encoding="utf-8")
print("Tamaño original:", df.shape)
print("Primeras filas (original):")
print(df.head(5).to_string())

# === Parte 2: detectar ===
dup_count = int(df.duplicated().sum())
na_initial = df.isna().sum().to_dict()

print("\nDetección:")
print("Duplicados encontrados:", dup_count)
print("NaN inicial por columna:", na_initial)

# === Parte 3: corregir ===

# 1) Eliminar duplicados
df2 = df.drop_duplicates().copy()

# 2) Rellenar NaN numéricos con la mediana
num_cols = df2.select_dtypes(include="number").columns
medianas = df2[num_cols].median(numeric_only=True)
df2[num_cols] = df2[num_cols].fillna(medianas)

# 3) Tratar outliers con IQR (y contar cuántos valores fueron recortados)
def iqr_clip_count(s: pd.Series):
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    before = s.copy()
    clipped = s.clip(low, high)
    changed = int((before != clipped).sum())
    return clipped, changed

outlier_changes = {}
for c in num_cols:
    df2[c], changed = iqr_clip_count(df2[c])
    outlier_changes[c] = changed

# Guardar limpio
df2.to_csv(clean_path, index=False, encoding="utf-8")

# === Parte 4: resumen ===
na_final = df2.isna().sum().to_dict()

# Hacemos un resumen sencillo en filas clave
summary_rows = [
    {"metric": "duplicados_eliminados", "valor": dup_count},
    {"metric": "na_inicial", "valor": na_initial},
    {"metric": "na_final", "valor": na_final},
    {"metric": "outliers_ajustados", "valor": outlier_changes},
]
pd.DataFrame(summary_rows).to_csv(summary_path, index=False, encoding="utf-8")

print("\n--- Verificación post-limpieza ---")
print("Tamaño limpio:", df2.shape)
print("Primeras filas (limpio):")
print(df2.head(5).to_string())
print("\nResumen guardado en:", summary_path.as_posix()) 