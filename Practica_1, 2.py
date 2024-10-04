print(" ") # print imprime un espacio

print("Briana Sarahi Sanchez Perez 3-W")
print(" ") # print imprime un espacio

thislist = ["Matematicas", "Español", "Ecosistemas", "Quimica", "Historia", "Ingles" ] # dando valores a la lista
# dando valores a la lista
calificaciones = {} # diccionario vacío

for thislist in thislist: # Hace algo con cada valor de la lista
    calificacion = input(f"Ingrese la calificacion obtenida en {thislist}: ")
    # pide la calificacion de la materia
    calificaciones[thislist] = calificacion
# almacena la calificación en el diccionario vacio

print(" ") # print imprime un espacio

for thislist, calificacion in calificaciones.items():
    # repite los elementos de el diccionario
    print(f"En {thislist} has obtenido {calificacion}.") 
    # print imprime las calificaciones para cada materia.

print(" ") # print imprime un espacio