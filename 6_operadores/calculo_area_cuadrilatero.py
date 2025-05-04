print('*** Sistema para calcular el área de un cuadrilátero ***\n')
base = float(input('Base: '))
altura = float(input('Altura: '))
area = base * altura
perimeter = 2 * (base + altura) #Precedencia de operadores
print('El área del cuadrilátero es: ', area)
print('\nEl perimetro del cuadrilátero es: ', perimeter)