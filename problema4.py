# Hacer el ejercicio de las tortugas del manual de practicas 

import turtle as tess


tess.shape("turtle")
tess.color("blue")
tess.speed(0)


def recorrido_recursivo(huellas, size):


    if huellas == 0:
        return


    tess.stamp()
    tess.forward(size)
    tess.right(24)
   
    recorrido_recursivo(huellas - 1, size + 3)


recorrido_recursivo(30, 3)


tess.done()

#a) Escribe el caso base: Cuando las huellas son 0
#b) Escribe el caso recursivo: recorrido_recursivo(huellas - 1, size + 3)
#c) Encuentra la ecuacion de recurrencia
#   T(n) = T(n-1)+1
#d) Encuentra la complejidad del algoritmo usando la solucion de ecuaciones de  recurrencia 
# Es identico al caso del problema1.py, por lo tanto: O(T(n)) = n


#al ejecutar en mi computadora si muestra la imagen 