# Error
# 1 ejercicio
try:
    num1 = float(input("Ingresa el primer número decimal: "))
    num2 = float(input("Ingresa el segundo número decimal: "))
    resultado = num1 / num2
    print("Resultado de la división:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Entrada no válida. Debes ingresar números decimales.")
except Exception as e:
    print("Error inesperado:", type(e).__name__)

# 2 ejercicio

edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

nombre = input("Ingresa un nombre para buscar la edad: ")

try:
    edad = edades[nombre]
    print(f"La edad de {nombre} es {edad}.")
except KeyError:
    print("Nombre no encontrado.")

# 3 ejercicio


def convertir_a_flotante(lista):
    try:
        return [float(i) for i in lista]
    except Exception as e:
        print("Error:", type(e).__name__)
    finally:
        print("Fin de la ejecución de la función")


print(convertir_a_flotante(['1.5', '2.7', 'texto']))


# 4 ejercicio
# Sin error
lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]
print(agrupar_listas(lista1, lista2))


def agrupar_listas(lista1, lista2):
    try:
        if len(lista1) != len(lista2):
            raise IndexError(
                "La cantidad de elementos en cada lista es diferente.")

        resultado = []
        for i in range(len(lista1)):
            suma = lista1[i] + lista2[i]
            resultado.append((lista1[i], lista2[i], suma))
        return resultado
    except Exception as e:
        print("Error:", type(e).__name__, "-", e)

# 5 ejercicio


respuestas = ['D', 'A', 'B', 'C', 'A']
tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], [
    'C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
tests_con_ex = [['D', 'A', 'B', 'C', 'A'], [
    'C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

calcular_notas(respuestas, tests_sin_ex)
calcular_notas(respuestas, tests_con_ex)


def calcular_notas(respuestas, tests):
    notas = []
    for test in tests:
        try:
            for r in test:
                if r not in ['A', 'B', 'C', 'D']:
                    raise ValueError(
                        f"La alternativa {r} no es una opción de alternativa válida")
            nota = sum(1 for r, t in zip(respuestas, test) if r == t)
            notas.append(nota)
        except ValueError as e:
            print("Error:", e)
            return
    print("Notas:", notas)

# 6 ejercicio


lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil','y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde','análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']

lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                    'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                    'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

# Prueba
try:
    validar_puntuacion(lista_tratada)
except ValueError as e:
    print("Error:", e)

try:
    validar_puntuacion(lista_no_tratada)
except ValueError as e:
    print("Error:", e)


def validar_puntuacion(lista_palabras):
    for palabra in lista_palabras:
        if any(p in palabra for p in [',', '.', '!', '?']):
            raise ValueError(
                f'El texto presenta puntuaciones en la palabra "{palabra}"')
    print("La lista no contiene puntuaciones.")
