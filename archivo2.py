#Leer un archivo "misdatos.txt" y mostrar su contenido
with open("misdatos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)