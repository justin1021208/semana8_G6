#Crea un programa que permita guardar n cantidad de notas en un archivo, leer notas, calcular el promedio, la nota mñas alta y la nota más baja.


n = int(input("¿Cuantas notas deseas ingresar?:"))
notas = []

for i in range(n):
    nota = float(input(f"Ingresa la nota {i+1}:"))
    notas.append(nota)

#Calcular promedio, maximo y minimo
promedio = sum(notas) / len(notas)
maximo = max(notas)
minimo = min(notas)

print("\nResultados:")
print("Notas ingresadas:", notas)
print("Promedio:", promedio)
print("Nota más alta:", maximo)
print("Nota más baja:", minimo)