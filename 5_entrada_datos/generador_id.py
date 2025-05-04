from random import randint

titulo_app = '*** Generador de ID único'
print(titulo_app)
nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
birthday = input('Ingresaa tu año de nacimiento (yyyy): ')

numero_aleatorio = randint(1000, 9999)
id_generado = f'{nombre.strip().upper()[:2]}{apellido.strip().upper()[:2]}{birthday.strip()[2:]}{numero_aleatorio}'
print(f'\nHola {nombre}, '
      f'\n\tTu nuevo número de ID generado es: \n\t{id_generado}\n\tFeliciades!')


