titulo_app = '*** Generador de Email ***'
nombre_usuario = '  Bolayo Granados Juarez    '
nombre_empresa = ' Ficness Club'
extension_dominio = '.com.mx'
nombre_usuario_normalizado = nombre_usuario.strip().lower().replace(" ", ".")
dominio_email_normalizado = '@' + nombre_empresa.strip().lower().replace(" ", "") + extension_dominio
print(titulo_app)
print(f'Nombre de usuario: {nombre_usuario}'
      f'\nNombre de usuario normalizado: {nombre_usuario_normalizado}'
      f'\n\nNombre empresa: {nombre_empresa}'
      f'\nExtension del dominio: {extension_dominio}'
      f'\nDominio de email normalizado: {dominio_email_normalizado}'
      f'\nEmail final generado: {nombre_usuario_normalizado + dominio_email_normalizado}')
