# Definición de la función

def cadena_digitada(cadena, n):
    for i in range(n):
        print(cadena)

# input

cadena = input("Digite el valor de la cadena: ")

n = int(input("Digita el número de veces que quieras que la cadena se repita: "))
cadena_digitada(cadena, n)