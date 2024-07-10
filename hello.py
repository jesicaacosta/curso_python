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

#operadores 

### Operadores Aritméticos ###

# Operaciones con enteros
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

#Operaciones con cadenas de texto
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print("Operaciones con enteros")
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print(" Operaciones con cadenas de texto")
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print("Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole ")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))