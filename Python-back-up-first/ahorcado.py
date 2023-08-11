import random 
import string

from ahorcado_diagrama import vidas_diccionario_visual
from palabras import lista_palabras #importamos solo el modulo palabras con el nombre palabras


 # obtener una palabra de una lista de plabras validas
def obtener_palabra_valida(lista_palabras): # palabras sera una lista de plabras validas en una rchivo separado
    #selecionar una palabra al azar de la lista de palabras validas
    palabra = random.choice(lista_palabras)
# para verificar que la palabra no tenga ningun caracter raro
    while '-' in lista_palabras or ' ' in lista_palabras: #mientras se cumpla esa condicion, continuar elegiando hasta elegir una plabra que no tenga - ni espacios
        palabra = random.choise(lista_palabras)
    return palabra.upper()


def ahorcado():

    print('===========================')
    print('==Bienvenido al AHORCADO===')
    print('===========================')

    palabra = obtener_palabra_valida(lista_palabras)
#una vez q tenemos la palabra necesitamso hacerle seguimiento a las letras en el juego
    letras_por_adivinar = set(palabra)  #estamos conviertiendo todas las letras de la pabra e un conjunto {'p', 'y', 't', 'o'}, 'n'}
    letras_adivinadas = set() #creamos un conjunt nuevo vacio

    abecedario = set(string.ascii_uppercase) # sin ñ, se lo podria agregar al conjunto, pero eso es otra historia
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f'te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}')

        # H - O L A Mostrar el estado actual de la palabra.
        palabra_lista = [letra if letra in letras_adivinadas
                         else '-' for letra in palabra]  # list comprension
        
        print(vidas_diccionario_visual[vidas]) #mostrar el estatus de la ahorca
        print(f'Palabra: {" ".join(palabra_lista)}') # mostrar las letras separadas por un espacio  estadoa actual del juego

        letra_usuario = input('Escoge una letra: ').upper()

        if letra_usuario in abecedario - letras_adivinadas: # si las letras elegidas por el usuario estan en el abecedari y no estan en el conjunto de las letras adivinadas
            #hay q agregar esa letra al conjunto de letras ya ingresadas
            letras_adivinadas.add(letra_usuario)   #abecedario - letras_adivinadas estamos erestadno dos conjuntos.
            #tenemos q preguntarnos estan en la palabra o no
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
            else:
                vidas -= 1
                print(f'tu Letra, {letra_usuario} no está en la palabra')
        #si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print('\n Ya escogiste esa letra, Por favor escoge una letra nueva') 
        else:
            print('esta letra no es valida')


# tenemos que llegar a un punto donde ya no quedan letras por adivinar o ya no quedan vidas

    if vidas == 0:
        print(f" Tienes {vidas_diccionario_visual[vidas]} vidas")
        print(f'AHORCADO, Perdiste, la palabra era {palabra}')

    else:
        print(f'GANASTE, adivinaste la palabra, esta era {palabra}')


ahorcado()