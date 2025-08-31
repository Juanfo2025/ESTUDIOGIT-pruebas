from utils.paths import REPORTS
REPORTS.mkdir(parents=True, exist_ok=True)
(REPORTS / "run.txt").write_text("Corrida OK: out.csv generado\n", encoding="utf-8")
