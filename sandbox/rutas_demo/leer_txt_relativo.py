# leer_txt_relativo.py — usa ruta relativa desde el directorio actual
# ejecuta este script desde la RAÍZ del repo
with open("sandbox/rutas_demo/notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print("Juan Forero Dice:")
print(contenido)
