import pandas as pd

# Cargar datasets
sucio  = pd.read_csv("ia_miniproyecto_02/datos_mp02.csv", encoding="utf-8")
limpio = pd.read_csv("ia_miniproyecto_02/datos_mp02_limpio.csv", encoding="utf-8")

# Tomar solo columnas numéricas (compatibles con cualquier versión de pandas)
num_sucio  = sucio.select_dtypes(include="number")
num_limpio = limpio.select_dtypes(include="number")

# Estadísticas
stats_sucio  = num_sucio.describe()
stats_limpio = num_limpio.describe()
diff = stats_limpio - stats_sucio

# Guardar reporte
report_path = "ia_miniproyecto_02/eda_mp03.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("=== mp03 – EDA: resumen inicial ===\n")
    f.write(f"Sucio shape:  {sucio.shape}\n")
    f.write(f"Limpio shape: {limpio.shape}\n\n")
    f.write("---- Stats sucio ----\n")
    f.write(stats_sucio.to_string() + "\n\n")
    f.write("---- Stats limpio ----\n")
    f.write(stats_limpio.to_string() + "\n\n")
    f.write("---- Diferencias (limpio - sucio) ----\n")
    f.write(diff.to_string() + "\n")

print("OK: ia_miniproyecto_02/eda_mp03.txt creado")

import matplotlib.pyplot as plt

def boxplot_comparado(s_antes, s_despues, titulo, ruta_png, etiqueta="valor"):
    a = s_antes.dropna()
    b = s_despues.dropna()
    plt.figure()
    plt.boxplot([a, b], labels=["antes", "después"], showmeans=True)
    plt.title(titulo)
    plt.ylabel(etiqueta)
    plt.tight_layout()
    plt.savefig(ruta_png)
    plt.close()

# Boxplots antes vs. después (edad y score)
boxplot_comparado(sucio["edad"],  limpio["edad"],  "Edad: antes vs. después",  "ia_miniproyecto_02/box_edad.png",  "edad")
boxplot_comparado(sucio["score"], limpio["score"], "Score: antes vs. después", "ia_miniproyecto_02/box_score.png", "score")

# (Opcional) Añadir percentiles al reporte
q_sucio  = num_sucio.quantile([0.25, 0.50, 0.75])
q_limpio = num_limpio.quantile([0.25, 0.50, 0.75])
with open(report_path, "a", encoding="utf-8") as f:
    f.write("\n---- Percentiles (0.25, 0.50, 0.75) ----\n")
    f.write("Sucio:\n"  + q_sucio.to_string()  + "\n\n")
    f.write("Limpio:\n" + q_limpio.to_string() + "\n")

print("Boxplots guardados: box_edad.png, box_score.png")

import numpy as np
import matplotlib.pyplot as plt

def hist_overlay(s_antes, s_despues, titulo, ruta_png, etiqueta="valor"):
    a = s_antes.dropna().astype(float)
    b = s_despues.dropna().astype(float)
    bins = np.histogram_bin_edges(pd.concat([a, b]), bins="auto")
    plt.figure()
    plt.hist(a, bins=bins, alpha=0.5, label="antes")
    plt.hist(b, bins=bins, alpha=0.5, label="después")
    plt.title(titulo)
    plt.xlabel(etiqueta)
    plt.ylabel("frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.savefig(ruta_png)
    plt.close()

# 1) Histogramas superpuestos
hist_overlay(sucio["edad"],  limpio["edad"],  "Edad: antes vs. después",
             "ia_miniproyecto_02/hist_edad_comparado.png",  "edad")
hist_overlay(sucio["score"], limpio["score"], "Score: antes vs. después",
             "ia_miniproyecto_02/hist_score_comparado.png", "score")

# 2) Conclusiones automáticas
def resumir_col(col):
    if col not in sucio.columns or col not in limpio.columns:
        return None
    s_a, s_d = sucio[col], limpio[col]
    def stats(s):
        s_num = pd.to_numeric(s, errors="coerce")
        return {
            "count_noNaN": int(s_num.dropna().shape[0]),
            "min": float(s_num.min()),
            "median": float(s_num.median()),
            "max": float(s_num.max()),
        }
    return stats(s_a), stats(s_d)

conclusiones_path = "ia_miniproyecto_02/conclusiones_mp03.txt"
with open(conclusiones_path, "w", encoding="utf-8") as f:
    f.write("=== mp03 – Conclusiones comparativas (antes vs. después) ===\n\n")
    for col in ["edad", "score"]:
        res = resumir_col(col)
        if res is None: 
            continue
        antes, despues = res
        f.write(f"- {col}:\n")
        f.write(f"  count sin NaN: {antes['count_noNaN']} → {despues['count_noNaN']}\n")
        f.write(f"  min:           {antes['min']} → {despues['min']}\n")
        f.write(f"  mediana:       {antes['median']} → {despues['median']}\n")
        f.write(f"  max:           {antes['max']} → {despues['max']}\n\n")

print("Listo: hist_edad_comparado.png, hist_score_comparado.png y conclusiones_mp03.txt")
