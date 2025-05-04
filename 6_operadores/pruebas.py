#Asignación encadenada
a = b = c = d = e = f = g = 'Hola mundo'
print(a)
#Cambiamos el valor de 'g' y de 'e'
g = 'Hola mundo G'
e = 'Hola mundo E'
print(f'a = {a}')
print(f'b = {b}')
print(f'e = {e}')
print(f'f = {f}')
print(f'g = {g}')
#Aunque pareciera que todas las variables apuntan al mismo objeto no es el caso cada una
#apunta a diferente espacio de memoria

#Asignación multiple con input
nombre, apellido = input('Escribe tu nombre y apellido separados por un tab: ').split('\t')
print(f'nombre: {nombre}, apellido: {apellido}')