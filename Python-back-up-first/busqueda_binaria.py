# Algoritmo de busqueda binaria para conseguir un elelmnto en especifico en una secuencia ordenado, es muhco mas eficiente 
# que uuna busqueda normal donde buscariamos elemento por elemento 

import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):  # esto va elemnto por elemento
        # ange(len(lista)): retorna 0, 1,2,3 4, 5... len-1
        if lista[i]  == objetivo:
            return i
    return -1 # en el caso de que el objtivo no este en la lista, su usa -1 para que se un indice valida que no puede cubrir otro caso,
    #solo cubre en el caso de que ele lemnento no pueda see r encontrado.

mi_lista = [1, 2, 3, 4, 5, 6, 7]
print(busqueda_ingenua(mi_lista, 5))




#como detrminamos eficiencia sobretodo cuando la lista es muhco mas larga

#ALGORITMO DE BUSQUEDA BIANRIA para optimizar
#para poder garantzar e=que le algoritmo fucnione la lista debe ser ordenada
def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 #inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista) - 1# fin de al  lista

    if limite_superior < limite_inferior:
        return -1 # esto termina la eecucion de la funcion y retornar -1
    # para implemntar busqueda binaria usaremos recusion

    punto_medio = (limite_inferior + limite_superior)//2  # solo retornar la parte entera

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio -1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio +1, limite_superior)
    

# if __name__ == '__main__':
#     mi_lista = [1, 2, 3, 4, 5, 6, 7]
#     print(busqueda_binaria(mi_lista, 5))

# evaluemos eficiencia/
# Primero Crearemos una lsita ordenada con 10 mil nmeros aleatorios
if __name__ == '__main__':
    tamaño = 20000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
    
    lista_ordenada= sorted(list(conjunto_inicial)) # lista ordenada con 10 mil elemento


#Vamoa a medir el tiempo de busqued ingenua 
inicio = time.time()
for objetivo in lista_ordenada: 
    busqueda_ingenua(lista_ordenada, objetivo)

fin = time.time()
print(f'tiempo de busqueda ingenua: {fin - inicio} segundos')


#Vamoa a medir el tiempo de busqued BINARIA

inicio = time.time()
for objetivo in lista_ordenada: 
    busqueda_binaria(lista_ordenada, objetivo)

fin = time.time()
print(f'tiempo de busqueda BINARIA: {fin - inicio} segundos')