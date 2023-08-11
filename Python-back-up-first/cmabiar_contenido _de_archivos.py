
with open('apuntes_curso_basico.txt', 'r') as archivo:
    for linea in archivo:
        print(linea)


notas = {
	'Nora' : 87,
	'Rodrigo' : 24,
	'Roberto' : 20
}

with open('data_students.txt', 'w') as archivo:
    for nombre, nota in notas.items():
        archivo.write(nombre + ' ' + str(nota) + '\n')
        

nuevas_notas = {
	'Javier' : 87,
	'Jony' : 24,
	'Mario' : 20
}
with open('data_students.txt', 'a') as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + ' ' + str(nota) + '\n')

        

