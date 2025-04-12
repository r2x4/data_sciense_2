##Crea un código para imprimir la suma de los elementos de cada una de las listas contenidas en la siguiente lista:

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

suma = [sum(x) for x in lista_de_listas]
print('Suma por listas:', suma)

## Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida en la siguiente lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

tercero = [tupla[0] for tupla in lista_de_tuplas]
print('Tercer elemento de las tuplas:', tercero)

## A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crea un código para generar una lista de tuplas en la que cada tupla tenga el primer elemento como la posición del nombre en la lista original y el segundo elemento siendo el propio nombre.

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
resultado = [(i, nombre) for i, nombre in enumerate(lista)]
print('tuplas pocicion y nombre:', resultado)

##Crea una lista usando la comprensión de listas (list comprehension) que almacene solo el valor numérico de cada tupla en caso de que el primer elemento sea 'Apartamento', a partir de la siguiente lista de tuplas:

alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

valor_apartamento = [x[1] for x in alquiler if x[0] == 'Apartamento']
print('Valor apartamento:', valor_apartamento)

### Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que las claves estén en la 

lista_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

diccionario = {mes: valor for mes, valor in zip (lista_meses, gasto)}
print('Diccionario:', diccionario)

### Una tienda tiene una base de datos con la información de venta de cada representante y de cada año y necesita filtrar solo los datos del año 2022 con ventas mayores a 6000. La tienda proporcionó una muestra con solo las columnas de los años y los valores de venta para que puedas ayudar a realizar la filtración de los datos a través de un código:

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

ventas_mayores_2022 = [(valor) for año, valor in ventas if año == '2022' and valor > 6000]
print('ventas mayores de 6000 en 2022:', ventas_mayores_2022)

###Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base de datos y le gustaría etiquetar los datos de la siguiente manera:

"""Glucosa igual o inferior a 70: 'Hipoglicemia'
Glucosa entre 70 y 99: 'Normal'
Glucosa entre 100 y 125: 'Alterada'
Glucosa superior a 125: 'Diabetes'
La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas usando la comprensión de listas que contenga la etiqueta y el valor de la glucemia en cada tupla."""

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

etiquetas_glicemia = [
    ('Hipoglicemia', valor) if valor <= 70 else
    ('Normal', valor) if 70 < valor <= 99 else
    ('Alterada', valor) if 100 < valor <= 125 else
    ('Deabetes', valor)
    for valor in glicemia
]
print('Etiquetas de glisemia:', etiquetas_glicemia)
