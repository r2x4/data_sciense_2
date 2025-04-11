# ejercicio 1
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# 1. Leer el tamaño de la lista
tamano = len(lista)
print(f"La lista tiene {tamano} números.")
# 2. Leer el valor máximo y mínimo
mayor = max(lista)
menor = min(lista)
print(f"El mayor es {mayor} y el menor es {menor}.")
# 3. Calcular la suma de los valores de la lista
suma = sum(lista)
print(f"La suma de los valores es {suma}.")
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor
print(
    f"La lista tiene {tamano} números, donde el mayor es {mayor} y el menor es {menor}. La suma de los valores es {suma}.")
# es `mayor` y el menor es `menor`. La suma de los valores es `suma`.
sum = mayor + menor
print(f"La suma de los valores es {sum}.")

# ejercicio 2 tablas de multiplicar

numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# ejercicio 3 multiplos de tres

lista_1 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
lista_2 = []
for numero in lista_1:
    if numero % 3 == 0:
        lista_2.append(numero)
print(f"Los números múltiplos de 3 son: {lista_2}")

# ejercicio 4

lista_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cuadrado(x): return x ** 2


lista_cuadrado = list(map(cuadrado, lista_3))
print(f"Los números al cuadrado son: {lista_cuadrado}")
