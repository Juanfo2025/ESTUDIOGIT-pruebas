import pandas as pd
from pathlib import Path

base = Path("ia_miniproyecto_02")
sucio  = pd.read_csv(base / "datos_mp02.csv", encoding="utf-8")
limpio = pd.read_csv(base / "datos_mp02_limpio.csv", encoding="utf-8")

def resumir(col):
    s_a = pd.to_numeric(sucio[col], errors="coerce")
    s_d = pd.to_numeric(limpio[col], errors="coerce")
    def stats(s):
        s = s.dropna()
        return {
            "count_noNaN": int(s.shape[0]),
            "min": float(s.min()),
            "median": float(s.median()),
            "max": float(s.max()),
        }
    return stats(s_a), stats(s_d)

lines = ["=== mp03 – Conclusiones comparativas (antes vs. después) ===\n"]
for col in ["edad", "score"]:
    antes, despues = resumir(col)
    lines.append(f"- {col}:")
    lines.append(f"  count sin NaN: {antes['count_noNaN']} → {despues['count_noNaN']}")
    lines.append(f"  min:           {antes['min']} → {despues['min']}")
    lines.append(f"  mediana:       {antes['median']} → {despues['median']}")
    lines.append(f"  max:           {antes['max']} → {despues['max']}\n")

out = base / "conclusiones_mp03.txt"
out.write_text("\n".join(lines), encoding="utf-8")
print(f"OK: {out.as_posix()} creado")
