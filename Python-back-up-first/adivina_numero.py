

#Adivina el numero. es un juego en el que el usuario va a adivinar un numero generado por la computadora
# el usuarion va a elegir un numeero y le vamos a decir si ese numero es mayor menor o igual al numero genrado por la compu

#definimos un a funcion q va a tener toda la logica del programa
import random


def adivina_el_num(x):  #la x va a representar elintervalo sup de numeros


    print('=========================')
    print('===Welcome to the game===')
    print('=========================')
    print('tu meta es adivinar el numero generado por la pc')

# 2 paso es hacer la funcionalidad dle juego
# vamos a usar una sentencia import para import random 
    numero_aleatorio = random.randint(1, x)  #randint retorna un entero aleatorio n, n esta entre 1 y x, por lo tanto necesito dos argunm

#logica principal del juego, q numero va a adivinar el usuario
    prediccion = 0 # es 0 para que no coincido con el numero aleatoreo
#como no sabemos cuantas veces necesitara el usaurio para adivinar el num, usamos un while
    while prediccion != numero_aleatorio:
        prediccion = int(input(f'adivina un num entre 1 y {x}: '))

        if prediccion < numero_aleatorio:
            print('intenta otra vez, este num es pequeño')
        elif prediccion > numero_aleatorio:
            print('intenta otra vez, este num es muy grande')
    print(f'Felicitaciones, adivinaste el numero {x} correctamente')


adivina_el_num(10)