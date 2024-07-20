
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
print ('----------------------- ')

# Multiline String with tree single quotes (comillas simples)
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print( 'La multilinea dice: ' , multiline_string)

long_text = """Este es un ejemplo de una cadena de texto
que abarca múltiples líneas. Puedes escribir libremente
y los saltos de línea serán respetados en la salida.

También puedes incluir 'singles quotes' y "doubles quotes"
sin necesidad de escape."""
print(long_text)

print ('----------------------- ')

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
print ('----------------------- ')

#### Unpacking (Desempaquetado) characters
language = 'PythonL'
a,b,c,d,e,f,g = language # unpacking sequence characters into variables 
print(a) # P le da el valor de la primer posicion del string
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n
print (g*5 + ' ' + f*6)


print('\n\n·········· Accessing characters in strings by index ········· ')
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1 
# Índices negativos:  -6 -5 -4 -3 -2 -1
# Elementos:          P  y  t  h  o  n
# Índices positivos:  0  1  2  3  4  5
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o


print('\n\n·········· Slicing (dividir ········· ')

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon


print('\n\n·········· Skipping character while splitting (segmentación) Python strings ········· ')
#secuencia[start:stop:step]
#start: Índice de inicio de la segmentación (incluido).
#stop: Índice de fin de la segmentación (excluido).
#step: Número de pasos a tomar entre cada índice.

skipping = 'Lklklklklk'
pto = skipping[0:10:2] 
print(pto) # Lllll


print('\n\n·········· Escape sequence ········· ')

print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')
#debe haber un \ para que tome el escape siguiente


print('\n\n·········· String Methods ········· ')

print('\n\n·········· capitalize ········· ')
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge) # 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

print('\n\n·········· count ········· ')
# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`


print('\n\n·········· endswith ········· ')

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('hon')) # True
print("La palabra finaliza con 'a'? {} " .format( challenge.endswith('a')) )  
print(f"La palabra finaliza con 'a'? {challenge.endswith('a')}") #solo para python 3.6

print('\n\n·········· expandstabs ········· ')
# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(15)) # 'thirty    days      of        python'

print('\n\n·········· find ········· ')
# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'

print(challenge.find('y'))  # 5
print(challenge.find('t')) # 0



print('\n\n·········· String Methods ········· ')

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = f'I am {first_name} {last_name}. I am a {job}. I live in {country}.' #mejor forma sin formatear
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.
ago = 30
print ('I am %s %s I am a %s I ago in %i'%(first_name, last_name, job, ago )) #mewjor forma para establecer el tipo de dato


radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0
resultado = radius + area
print ( ' el resultado es %s ' %(resultado))
print ( ' el resultado es %i ' %(resultado))


# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0


print('\n\n·········· isalnum ········· ')

# isalnum(): Checks alphanumeric character
#Verifica si todos los caracteres en la cadena son alfanuméricos 
# (letras y números) y no está vacía.

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True
challenge = 'ThirtyDaysPython!34'
print(challenge.isalnum()) # False
challenge = 'thirty days of python'
print(challenge.isalnum()) # False


print('\n\n·········· isalpha ········· ')

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

print('\n\n·········· isdecimal ········· ')

# isdecimal(): Checks Decimal Characters

num = '10'
print(num.isdecimal()) # True, porque '10' son dígitos decimales.
num = '10.5'
print(num.isdecimal()) # False, porque '10.5' tiene un punto decimal.


print('\n\n·········· isdigit ········· ')
# isdigit(): Checks Digit Characters , si todos son numeros
challenge = 'Thirty1'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True


print('\n\n·········· isdecimal ········· ')
# isdecimal():Checks decimal characters
num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


print('\n\n·········· isidentifier ········· ')
# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
#verifica si una cadena puede ser utilizada como un identificador válido, como el nombre de 
# una variable.Debe comenzar con una letra o guion bajo y puede contener letras, números o guiones bajos.

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


print('\n\n·········· islower ········· ')

# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

print('\n\n·········· isupper ········· ')

# isupper(): Checks if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


print('\n\n·········· isnumeric ········· ')

# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False


print('\n\n·········· join ········· ')

# join(): Returns a concatenated string
#Une una lista de cadenas con un separador especificado.

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' ★ \t'.join(web_tech)
print(result) # HTML ★  CSS ★   JavaScript ★    React
result = ' , '.join(web_tech)
print(result) #HTML , CSS , JavaScript , React


print('\n\n·········· strip ········· ')
# strip(): Removes both leading and trailing characters
#Elimina los caracteres especificados del principio y el
# final de la cadena. Por defecto, elimina espacios.

challenge = ' thirty days of python '
print(challenge.strip()) # 5

print('\n\n·········· REPLACE ········· ')
# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('py', 'Agregado')) # elimina py,agrega agregado y y lo que resta


print('\n\n·········· split ········· ')
# split():Splits String from Left
#Divide la cadena en una lista usando un separador. Por defecto, usa cualquier espacio en blanco.
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']



# title(): Returns a Title Cased String
#Convierte la primera letra de cada palabra en mayúscula y el resto en minúscula.
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python


# swapcase(): Change all lowercase letters to uppercase and vice versa.
#Cambia todas las letras minúsculas por mayúsculas y viceversa.

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


# startswith(): Checks if String Starts with the Specified String
#Verifica si la cadena comienza con la subcadena especificada.
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False