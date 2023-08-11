#la computadora es la q va a adivinar el  numero.
import random


def adivina_el_numero_pc(x):
    print('=========================')
    print('===Welcome to the game===')
    print('=========================')
    print(f'Selecciones un número entre 1 y {x}')
    limite_inferior = 1 # (1, x)
    limite_superior = x

    respuesta = ''

    while respuesta != 'c':  # c es la letra q el usuario  va a tener q ingresar para confirmar q la compu elegio el valor coreecto
    #generar prediccion
        if limite_inferior != limite_superior: # (1 y 10)
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # o tb = limite superior ya que ambos osn iguales enste caso
        #obtener la respuesta del usuario
        respuesta = input(f'Mi prediccion es {prediccion}. Si es mas baja ingresa (A) y Si es mas alta ingresa (B), Y si es correcto ingresa C: ').lower()  # lo q dice la pc
        
        if respuesta == 'a':
            limite_superior = prediccion - 1 # restamos uno a la prediccion de la pc, xq el num predicho por la pc no es el correcto entonces lo descontamos por la opcion 'a'
        elif respuesta == 'b':
            limite_inferior = prediccion + 1
    print(f'SIIII la pc adivinó tu numero correctamente {prediccion}')


adivina_el_numero_pc(10)
