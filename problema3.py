#Diseña un algoritmo recursivo que imprima una cadena al reves 

def cadena_Reves(cadena):

    if cadena == "":
        return

    cadena_Reves(cadena[1:])#O(n)

    #  esto imprime después de regresar
    print(cadena[0])


c = "Buenas"

cadena_Reves(c)

#a) Escribe el caso base: Cuando la cadena esta vacia  
#b) Escribe el caso recursivo: cadena_Reves(cadena[1:])
#c) Encuentra la ecuacion de recurrencia
#   T(n) = T(n-1)+n
#d) Encuentra la complejidad del algoritmo usando la solucion de ecuaciones de  recurrencia 
# Como en el caso anterior en problema2.py  es el mismo
# Por lo tanto T(n) = n(n+1) / 2
# O(T(n)) = n^2