# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


""" edad = int (input("Escriba su edad: "))

def aniosCumplidos (anios): 
    
    for i in range (1, anios + 1):

        print ("Cumpliste ", i) 

aniosCumplidos(edad)

print( aniosCumplidos) """


# age = int(input("¿Cuántos años tienes? "))
# for i in range(age):
#     print("Has cumplido " + str(i+1) + " años")


# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas


""" numeroEnteroPositivo = int (input("Escriba un número entero positivo: "))

lista = [ ]

def numerosPositivos (numero):

    while numero >= 0:

        lista.append(numero)

        numero -= 1
    
    print(lista)

numerosPositivos(numeroEnteroPositivo)

print(numerosPositivos) """



# n = int(input("Introduce un número entero positivo: "))
# for i in range(n, -1, -1):
#     print(i, end=", ")





# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

""" invertir = int (input("Cantidad a invertir: "))
interes = int (input("El interes es: "))
anios = int (input("Años de inversión: "))
d = 365                                         #Días de año
m = 12                                   #Meses del año


def inversion (cantidadInvertir, ganaInteres, tiempoDeposito):

    i = 1

    while i <= anios :
    

        interesMensual = (cantidadInvertir * ( (ganaInteres/100) * (interes/d)  ) ) 

        interesAnual = interesMensual * m * i

        totalGanancia = interesAnual + cantidadInvertir

        print("El capital ", cantidadInvertir, "en un tiempo de ", i , "año, genera una ganacia de: ", round(totalGanancia, 2) )

        i += 1 



inversion(invertir, interes, anios)

print (inversion) """







""" invertir = int (input("Cantidad a invertir: "))
interes = int (input("El interes es: "))
anios = int (input("Años de inversión: "))
i = 365                                         #Días de año
m = 12                                   #Meses del año

def inversion (cantidadInvertir, ganaInteres, tiempoDeposito):

    for c in range(1, anios+1) :

      interesMensual = (cantidadInvertir * ( (ganaInteres/100) * (interes/i)  ) ) 

      interesAnual = interesMensual * m * c

      totalGanancia = interesAnual + cantidadInvertir

      print("El capital ", cantidadInvertir, "en un tiempo de ", c , "año, genera una ganacia de: ", round(totalGanancia, 2) )

inversion(invertir, interes, anios)

print (inversion) """




# amount = float(input("¿Cantidad a invertir? "))
# interest = float(input("¿Interés porcentual anual? "))
# years = int(input("¿Años?"))
# for i in range(years):
#     amount *= 1 + interest / 100 
#     print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2))



# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

""" numero = int (input("Ingrese un número entero positivo: "))

def numeroPrimo(num):
    
    contador = 0

    for i in range (1, num+1):

        if num % i == 0:

            contador += 1 
    
    if contador == 2:
        print ("El número: ", num, " es primo")
    
    else:
        print ("El número: ", num, " no es primo")


numeroPrimo(numero)

print(numeroPrimo) """




# n = int(input("Introduce un número entero positivo mayor que 2: "))
# i = 2
# while n % i != 0:
#     i += 1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")



# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

""" palabra = str (input("Escriba unja palabra  "))

def reversa (pal):

    for i in range (len(pal)-1, -1, -1 ):

        print(pal[i], end = "")

reversa(palabra)

print(reversa) """







""" palabra = str (input("Escriba unja palabra  "))

def reversa (pal):
    
    resultado = ""                      #Cadena vacía
    cantidad = len (pal)

    while cantidad > 0 :

        resultado += pal [ cantidad - 1 ]   #Posicion menos 1 

        cantidad -= 1

    print (resultado)

reversa(palabra)

print(reversa) """




# word = input("Introduce una palabra: ")
# for i in range(len(word)-1, -1, -1):
#     print(word[i])





# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


""" introduzcaPalabra = str (input("Introduzaca algún caracter: "))

palabraFin = "salir"

def introducir (palabra):

    while palabra != palabraFin :

        palabra = str (input("Introduzaca algún caracter: "))


introducir(introduzcaPalabra)

print(introducir) """




# while True:
#     frase = input("Introduce algo: ")
#     if frase == "salir":
#         break
#     print(frase)



# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función


""" diametro = float (input("Introduzca el diametro: "))

radio = round (diametro/2, 2)

pi= 3.14

def circulo (calcular):

    area = pi * (radio * radio)

    volumen =  (4/3) * pi * radio * radio * radio 

    print("El área de su círculo es: ", area)

    print ("El volumen de su círculo es: ", volumen)


circulo (diametro)

print ( circulo) """





# def circle_area(radius):
#     """Función que calcula el area de un círculo.
#     Parámetros
#     radius: Es el radio del círculo.
#     Devuelve el área del círculo de radio radius. 
#     """
#     pi = 3.1415
#     return pi*radius**2

# def cilinder_volume(radius, high):
#     """Función que calcula el volumen de un cilindro.
#     Parámetros
#     radius: Es el radio de la base del cilindro.
#     high: Es la altura del cilindro.
#     Devuelve el volumen del clindro de radio radius y altura high.
#     """
#     return circle_area(radius)*high

# print(cilinder_volume(3,5))



# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial


""" numeroPositivo = int (input("Escriba un número positivo: "))


def factorial (numero):

    producto = 1 

    i = 1 

    while i <= numero:

        producto = producto * i

        i += 1

        
    print("El factorial de ", numero, "! es: ", producto)

factorial (numeroPositivo)

print (factorial) """



# def factorial(n):
#     """Función que calcula el factorial de un número entero positivo.
#     Parámetros
#     n: Es un entero positivo.
#     Devuelve el factorial de n.
#     """
#     tmp = 1
#     for i in range(n):
#         tmp *= i+1
#     return tmp


# print(factorial(4))
# print(factorial(20))



# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.


""" lista= [10,20,40,80 ]

cantidad= len(lista)

def media(list):
    
    sumaLista= 0
    
    for i in list:
    
        sumaLista += i
    
    media = sumaLista / cantidad
    
    print ("La media es: ", media)

media(lista)

print(media) """




# def mean(sample):
#     """Función que calcula la media de una muestra de números.
#     Parámetros
#     sample: Es una lista de números
#     Devuelve la media de los números en sample. 
#     """
#     return sum(sample)/len(sample)

# print(mean([1, 2, 3, 4, 5]))
# print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))





# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

""" def saludar (): 
    saludo = "!Hola amiga¡"

    print (saludo)

saludar()
print(saludar) """


# def greet():
#     """Función que muestra el saluco ¡Hola amiga! por pantalla."""
#     print('¡Hola amiga!')
#     return

# greet()