print('*** Sistema de autenticacion ***\n')
usuario_valido = 'pancho'
password_valido = '123'
user = input('Cual es tu usuario? ').strip().lower()
password = input('Cual es tu password? ').strip().lower()
print(f'{usuario_valido == user and password == password_valido}')

