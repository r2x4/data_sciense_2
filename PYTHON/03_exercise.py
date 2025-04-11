# ejercicio 5

def ingresar_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero_nota} (0-5): "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 5")
        except ValueError:
            print("Error: Ingrese un número válido")

# Ingreso de notas con validación
nota1 = ingresar_nota(1)
nota2 = ingresar_nota(2)
nota3 = ingresar_nota(3)
nota4 = ingresar_nota(4)
nota5 = ingresar_nota(5)

notas = [nota1, nota2, nota3, nota4, nota5]

# Asegúrate de que no hayas usado "sum" como variable antes
promedio = lambda n: sum(n) / len(n)
media = promedio(notas)

mayor = max(notas)
menor = min(notas)

situacion = "Aprobado(a)" if media >= 3.0 else "Reprobado(a)"

print(f"El estudiante obtuvo una media de {media:.2f}, con la mayor nota de {mayor} puntos y la menor nota de {menor} puntos y fue {situacion}.")