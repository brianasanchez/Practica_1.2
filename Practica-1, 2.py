print(" ") # print imprime un espacio

print("Briana Sarahi Sanchez Perez 3-W")
print(" ") # print imprime un espacio

thislist = [] # lista vacia

numeros = 5 # cantidad de numeros

for n in range(numeros): # Hace algo con cada valor de los numeros
    numero = int(input(f"Ingrese el número triunfador {n + 1}: "))
    # pide ingresar el numero triunfador
    thislist.append(numero) # agrega un elemento al final 

print(" ") # print imprime un espacio

thislist.sort() # Se ordenan los elementos

print("Los números triunfadores de la lotería, ordenados de menor a mayor, son:")
# imprime texto
print(thislist) # imprime lista

print(" ") # print imprime un espacio