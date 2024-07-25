#lists

my_list = list()  #creop una lista
my_list= ["Jesica", 30, 1.70, "aa","aa", "bb" ,"aaaaa"]

print (type(my_list))
print (len(my_list))
print (my_list[1])
#print (my_list[-6]) IndexError: list index out of range

#asigno un elemento de la lista a una variable
nombre = my_list[0]

#Desempaquetado Unpacking de una lista, asigno nombre a cada uno de los valores de la lista
name, age, height, letra, letraA, ltraB, ltraA = my_list
print(age)

#name, age, height, letra, letraA, ltraB = my_list #ValueError: too many values to unpack (expected 6) 
#error porque debe tener nombre para todos los elementos de la lista 


# Metodos para listas 
#count retorna el nro de ocurrencia de un valor
print(my_list.count('aa')) #2

my_other_list = ['diego' , 39 ]

print(my_list + my_other_list) 


#tipado debil, dinamico, se puede cambiar cambiando el valor
print(type(my_list))
my_list = 'Jes'
print(type(my_list))













