#Diseña un algoritmo recursivo quer imprima todos los elementos de un arreglo
#a) Escribe el caso base 
#b) Escribe el caso recursivo 
#c) Encuentra la ecuacion de recurrencia 
#d) Encuentra la complejidad del algoritmo usando la solucion de ecuaciones de  recurrencia  

def imprimir_arreglo(array):
    if len(array) == 0:
        return
    
    print(array[0])

    imprimir_arreglo(array[1:])#O(n)

lista = [1, 2, 5, 6]
imprimir_arreglo(lista)

#a) El caso base es que la longitud del arreglo sea 0
#b) El caso recursivo es que se llama a la funcion a si misma 
#imprimiendo los elementos del arreglo hasta que su longitud sea 0
#c)La ecuacion de recurrencia es: T(n) = T(n-1) + n
#d) T(n) = n + T(n-1)
#   T(n) = n(n+1) / 2
#   O(T(n)) = n^2

    