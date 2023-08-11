#Piedra paepl o tijera
import random


def jugar():  #la funcion no necesita ningun  valor
    usuario = input('Escoge una opcion, "pa" para papel, "pi" para piedra, "ti" para tijera:\n').lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!!!'
    # para saber quien ganó hacemos una funcion dentro de la funcion jugar
    if gano_el_jugador(usuario, computadora): # CAMPARAMOS LA SELECCION DEL USUARIO CON LA SELECCION DE LA PC
        return 'GANASTE'
    

    # si el usuario no ganó
    return 'Perdiste!!!'


def gano_el_jugador(jugador, oponente):
    # retornar true si gana el jugador
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else: 
        return False
    

print(jugar())
