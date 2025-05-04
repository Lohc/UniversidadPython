titulo_app = '*** Receta de cocina ***'
nombre_plato = input('Ingresa el nombre del plato: ')
ingredientes = input('Ingresa los ingredientes: ')
tiempo_preparacion = input('Ingresa el tiempo de preparación (min): ')
dificultad = input('Ingresa la dificultad: ')

print(f'-'*20)
print(titulo_app)
print(f'Nombre receta: {nombre_plato}'
      f'\nIngredientes: {ingredientes}'
      f'\nTiempo de preparacion: {tiempo_preparacion}'
      f'\nDificultad: {dificultad}')