#Diseña un algoritmo recursivo que calcule la suma de los primeros n numeros naturales 
#a) Escribe el caso base 
#b) Escribe el caso recursivo 
#c) Encuentra la ecuacion de recurrencia 
#d) Encvuentra la complejidad del algoritmo usando la solucion de ecuaciones de  recurrencia  

#a) CASO BASE: cuando natural = 1
#b) CASO RECURSIVO: cuando natural es diferente de 1 entonces 
# hace llamado a la funcion SumaNaturales(natural - 1) y se le suma natural

def SumaNaturales(natural):
    if natural > 0:
        if natural == 1:
            return 1
        else:
            return natural + SumaNaturales(natural - 1)

natural = 6        
print("La suma natural de {} es: {} ".format(natural, SumaNaturales(natural)))

#Ecuacion de recurrencia: T(n) = T(n-1) + 1
# T(1) = 1
#d) T(n) - T(n-1) = 1
#   (x-1)(x-1) = 0
#   T(n) = C1 + C2n
# En calse ya hemos resulto varias veces esta ecuacion asi que:
# T(n) = 1 + n
# O(T(n)) = n

