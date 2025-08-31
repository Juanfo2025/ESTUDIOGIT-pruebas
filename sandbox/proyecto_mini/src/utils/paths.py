from pathlib import Path

AQUI = Path(__file__).resolve().parent           # .../src/utils
PROYECTO = AQUI.parent.parent                    # .../proyecto_mini

DATA = PROYECTO / "data"
RAW = DATA / "raw"
PROCESSED = DATA / "processed"
REPORTS = PROYECTO / "reports"
