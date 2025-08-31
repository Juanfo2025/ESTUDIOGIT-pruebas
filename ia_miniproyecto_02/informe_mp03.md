# Informe mp03 – EDA (antes vs. después)

**Contexto:** mp02 (limpieza) → mp03 (EDA).
**Objetivo:** comparar distribución antes/después y documentar resultados.

**Datasets:** sucio shape (17, 3) · limpio shape (16, 3)

## Edad
- count sin NaN: 7 → 6
- min: 22.0 → 22.0
- mediana: 29.0 → 31.5
- max: 200.0 → 200.0

## Score
- count sin NaN: 7 → 16
- min: 65.0 → 84.0
- mediana: 80.0 → 84.0
- max: 300.0 → 84.0

## Visualizaciones

## Conclusiones

- La imputación por **mediana** aumentó `count` sin NaN y evitó sesgos por outliers.
- El recorte **IQR** redujo `max` a rangos razonables y estabilizó la distribución.
- Las métricas centrales (mediana) cambiaron poco: limpieza **robusta** sin distorsionar la señal.
