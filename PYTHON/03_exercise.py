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

#  ejercicio 6

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

nombres = list(map(lambda x: x.capitalize(), nombres))
apellidos = list(map(lambda x: x.capitalize(), apellidos))
nombres_completos = list(map(lambda x, y: f"{x} {y}", nombres, apellidos))
print(nombres_completos)

# ejercicio 7

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

def calcula_puntos(goles_marcados, goles_recibidos):
    puntos = 0
    total_partidos = len(goles_marcados)
    
    for marcados, recibidos in zip(goles_marcados, goles_recibidos):
        if marcados > recibidos:
            puntos += 3
        elif marcados == recibidos:
            puntos += 1
        # Si pierde, no suma puntos

    max_puntos = total_partidos * 3
    rendimiento = (puntos / max_puntos) * 100 if max_puntos > 0 else 0

    return puntos, round(rendimiento, 2)


puntos, rendimiento = calcula_puntos(goles_marcados, goles_recibidos)
print(f"Puntos conseguidos: {puntos}")
print(f"Rendimiento: {rendimiento}%")

# ejercicio 8

# Datos base
distancias = {
    "Salvador": 850,
    "Fortaleza": 800,
    "Natal": 300,
    "Aracaju": 550
}

gastos_paseo_dia = {
    "Salvador": 200,
    "Fortaleza": 400,
    "Natal": 250,
    "Aracaju": 300
}

# Constantes
costo_hotel_dia = 150
consumo_km_litro = 14
precio_gasolina_litro = 5

# Función para calcular el gasto de hotel
def gasto_hotel(dias):
    return dias * costo_hotel_dia

# Función para calcular el gasto de gasolina (ida y vuelta)
def gasto_gasolina(ciudad):
    distancia_total = distancias[ciudad] * 2
    litros_necesarios = distancia_total / consumo_km_litro
    return litros_necesarios * precio_gasolina_litro

# Función para calcular el gasto de paseo y alimentación
def gasto_paseo(ciudad, dias):
    return gastos_paseo_dia[ciudad] * dias

# Simulación de viaje
def calcular_gasto_total(ciudad, dias):
    total = gasto_hotel(dias) + gasto_gasolina(ciudad) + gasto_paseo(ciudad, dias)
    return round(total, 2)

# Prueba del viaje a Salvador por 3 días
ciudad_destino = "Salvador"
dias_viaje = 3
gasto_total = calcular_gasto_total(ciudad_destino, dias_viaje)

print(f"Con base en los gastos definidos, un viaje de {dias_viaje} días a {ciudad_destino} desde Recife costaría {gasto_total} reales.")

#ejercicio 9

# Frase de prueba
frase = "Aprender Python aquí en Alura es muy bueno"

# Reemplazar signos de puntuación por espacios (en este caso no hay, pero dejamos el paso por si se generaliza)
frase = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')

# Separar la frase en palabras
palabras = frase.split()

# Filtrar las palabras con 5 o más caracteres usando lambda y filter
palabras_filtradas = list(filter(lambda palabra: len(palabra) >= 5, palabras))

# Mostrar el resultado
print(palabras_filtradas)

