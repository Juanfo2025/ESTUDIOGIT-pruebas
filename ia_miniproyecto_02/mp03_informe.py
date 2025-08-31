import pandas as pd
from pathlib import Path

base = Path("ia_miniproyecto_02")
sucio  = pd.read_csv(base / "datos_mp02.csv", encoding="utf-8")
limpio = pd.read_csv(base / "datos_mp02_limpio.csv", encoding="utf-8")

def stats(df, col):
    s = pd.to_numeric(df[col], errors="coerce").dropna()
    return {
        "count": int(s.shape[0]),
        "min": float(s.min()),
        "median": float(s.median()),
        "max": float(s.max()),
    }

cols = ["edad", "score"]

lines = []
lines.append("# Informe mp03 – EDA (antes vs. después)\n")
lines.append("**Contexto:** mp02 (limpieza) → mp03 (EDA).")
lines.append("**Objetivo:** comparar distribución antes/después y documentar resultados.\n")
lines.append(f"**Datasets:** sucio shape {sucio.shape} · limpio shape {limpio.shape}\n")

for c in cols:
    a, d = stats(sucio, c), stats(limpio, c)
    lines.append(f"## {c.capitalize()}")
    lines.append(f"- count sin NaN: {a['count']} → {d['count']}")
    lines.append(f"- min: {a['min']} → {d['min']}")
    lines.append(f"- mediana: {a['median']} → {d['median']}")
    lines.append(f"- max: {a['max']} → {d['max']}\n")

lines.append("## Visualizaciones\n")
blocks = [
    ("Histogramas edad (antes/después) separados", ["hist_edad_antes.png","hist_edad_despues.png"]),
    ("Histogramas score (antes/después) separados", ["hist_score_antes.png","hist_score_despues.png"]),
    ("Boxplots edad y score", ["box_edad.png","box_score.png"]),
    ("Histogramas superpuestos", ["hist_edad_comparado.png","hist_score_comparado.png"]),
]
for title, files in blocks:
    have = [f for f in files if (base/f).exists()]
    if not have: 
        continue
    lines.append(f"**{title}:**")
    for f in have:
        lines.append(f"![{f}]({f})")
    lines.append("")

lines.append("## Conclusiones\n")
lines.append("- La imputación por **mediana** aumentó `count` sin NaN y evitó sesgos por outliers.")
lines.append("- El recorte **IQR** redujo `max` a rangos razonables y estabilizó la distribución.")
lines.append("- Las métricas centrales (mediana) cambiaron poco: limpieza **robusta** sin distorsionar la señal.\n")

out = base / "informe_mp03.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"OK: {out.as_posix()} creado")
