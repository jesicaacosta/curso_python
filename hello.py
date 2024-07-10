nombre = 'Jesica'
# comment
print('Hola mi nombre es' ,nombre)

saludo = "Hola"
mensaje = saludo + ", " + nombre
longitud = len(mensaje)
mayusculas = mensaje.upper() 

#consulta tipo de dato 
print(type( mayusculas )) 
print(type( 1 )) 
print(type( 1.2 )) 
print(type( True ))  #<class 'bool'>
print(type( 1+4j )) #<class 'complex'>
print(type( print(mayusculas))) #<class 'NoneType'>

'''
mensaje
de varias
lineas 
'''

print( ' El largo es: ' , longitud , ' y el mensaje en mayusculas es: ' , mayusculas) 

#varias variables (no recomendable)

name, surname, age, alias = 'Jesica' , 'Acosta' , 30 , 'jesidaiq'

print ('Mi nombre es ' ,name, surname, 'tengo ' , age, 'Instagram es ' ,alias)
print(type (alias))

agee = input('How old are you? ') 

print('Tu edad es ',agee)