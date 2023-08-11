# organizacion = 'freecodecamp'
# print('aprende a programar con 1 ' + organizacion)

# print('aprende a programar con 2 {}'.format(organizacion))

# print(f'Aprende a programar con 3 {organizacion}') #fstring



# Mad Libs Historias locas
#primero necesitamos un parrafo en el cual podamos sustituir o reemplazar las palabras que el usuario introduzca. guardamos ese parrafo en una nueva variable maplib.
#segundo necesatamos un adjetivo, verb1 y 22
adj = input('adjetivo: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
sustantivo_plural = input('Sustantivo_plural: ')
#primero creamos la pklantilla que vamos a rellenar
madlib = f'!programar es tan {adj}!. Siempre me emociona porque me encanta {verb1} problemas. Aprende a {verb2} con freecodecamp y alcanza tus {sustantivo_plural}'

print(madlib)


