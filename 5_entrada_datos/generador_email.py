print('*** Generador de Email ***')
nombre = input('Nombre(s): ')
apellido = input('Apellido(s): ')
nombre_empresa = input('Nombre Empresa: ')
extension_dominio = input('Extension dominio: ')

email = (f'{nombre.strip().lower().replace(" ",".")}.'
         f'{apellido.strip().lower().replace(" ",".")}@'
         f'{nombre_empresa.strip().lower().replace(" ", "")}'
         f'{extension_dominio}')

print(email)