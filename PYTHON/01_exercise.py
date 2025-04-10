# ejercicio 3 aleatorio

import random

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

aleatorio = random.choice(lista)
print(aleatorio)

# ejercicio 4  numero aleatorio de 1  100

numero_ale = random.randint(1, 100)
print(numero_ale)

# ejercicio 5 potencia

num1 = int(input("Introduce primer numero: "))
num2 = int(input("Introduce segundo numero: "))
potencia = num1 ** num2
print(f"La potencia de {num1} elevado a {num2} es: {potencia}")

# ejercicio 6 perdir numero

num_participantes = int(input("cuantos participantes hay en sorteo:"))

if num_participantes > 0:
    ganador = random.randint(1, num_participantes)
    print(f"El ganador es el participante numero {ganador}")
else:
    print("El numero de participantes debe ser mayor a 0")

# ejercicio 7

nombre_usuario = input("Introduce tu nombre: ")
numero_tiket = random.randint(1000, 9998)
print(f"Hola {nombre_usuario}, tu numero de tiket es: {numero_tiket}")

# ejercicio 8

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco",
        "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

fruta_aleatoria = random.sample(frutas, 3)
print("Las frutas elegidas son:")
for fruta in fruta_aleatoria:
    print(fruta)

### ejercicio 9 raiz cuadrada

import math

numeros = [2, 8, 15, 23, 91, 112, 256, 144, 36, 25]
print("Números con raíz cuadrada entera:")

for numero in numeros:
    raiz = math.sqrt(numero)
    if raiz.is_integer():
        print(f"{numero} → raíz cuadrada: {int(raiz)}")

### ejercicio 10

import math

precio_m2 = 50000
radio = float(input("Introduce el radio del terreno en metros: "))
area = math.pi * radio ** 2
precio_total = area * precio_m2
print(f"El precio total del terreno es: {precio_total:.2f} pesos")
