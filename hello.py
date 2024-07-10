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

#agee = input('How old are you? ') 


#operadores 

### Operadores Aritméticos ###

# Operaciones con enteros
a = 200
b = 5
remainder = a % b
floor_division = a // b
exponential = a ** b

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

#Operaciones con cadenas de texto
print("Hola " + str(5))

# Operaciones mixtas
print("Hola - " * 5) #Hola Hola Hola Hola Hola
print("Hola " * (2 ** 2))

my_float = 2.5 * 2 ##el resultado es 5 
print("Hola my_float" * int(my_float)) #multiplica 5 veces el string

### Operadores Comparativos ###

print("Operaciones con enteros")
print(3 == 4) #false 
print(3 != 4) #true 
print("Hola" > "Python") #false 
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")

### Operadores Lógicos ###

print("Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole ")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))