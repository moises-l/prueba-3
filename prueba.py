
filas = 10
columnas = 15
asientos = []
for fila in range(filas):
    fila_asientos = []
    for columna in range(columnas):
        fila_asientos.append(f"{chr(65 + fila)}{columna+1}")
    asientos.append(fila_asientos)



def mostrar_menu():
    print("\n--- CINE DUOC ---")
    print("1. Mostrar Peliculas disponibles.")
    print("2. Mostrar asientos disponibles.")
    print("3. Comprar entradas.")
    print("4. Salir.")

def nueva_pelicula():
    nombre = input("Ingrese el nombre de la pelicula")
    descripción = print("Pelicula sobre una araña que muerde a una persona")
    categoria = print("Acción")
    peliculas[nombre] = {"descripción": descripción, "categoria": categoria, "ventas": 0, "asistentes": []}
    print("Pelicula seleccionada correctamente")


def mostrar_peliculas():
    print("1. Spiderman - Lejos de Casa")
    print("2. El Rey León")
    print("3. Toy Story 4")
    print("4. Scream IV")
    print("5. Super Mario Bros 2D")
    print("6. Super Mario Bros 3D")
    print("7. Avatar 3D")



def mostrar_asientos():
    print("Mapa de asientos:")
    for fila in asientos:
        for asiento in fila:
            print(asiento, end=" ")
        print()

def comprar_entrada():
     mostrar_asientos()
     asiento_seleccionado = input("Ingrese el asiento que desea reservar (por ejemplo, A1): ")
     if asiento_seleccionado in [asiento for fila in asientos for asiento in fila]:
         nombre_pelicula = input("Ingrese el nombre de la pelicula")
         if nombre_pelicula in peliculas:
            pelicula = peliculas[nombre_pelicula]
            fila, columna = obtener_fila_columna_asiento(asiento_seleccionado)
            if asientos[fila][columna] != "X":
                 asientos[fila][columna] = "X"
                 pelicula["ventas"] += 1
                 pelicula["asistentes"].append(asiento_seleccionado)
                 generar_boucher(asiento_seleccionado, nombre_pelicula, pelicula["ventas"])
                 print("Reserva exitosa")
            else:
                 print("Lo siento, el asiento seleccionado ya esta ocupado")
         else: 
             print("No se encontró la pelicula ingresada")
     else: 
         print("El asiento seleccionado no es valido")

def obtener_fila_columna_asiento(asiento):
     fila = ord(asiento[0]) - 65
     columna = int (asiento[1:]) - 1
     return fila, columna

def generar_boucher(asiento, pelicula, numero_boleta):
    with open("boucher.txt", "a") as archivo:
        archivo.write(f"numero de boleta: {numero_boleta}\n")
        archivo.write(f"asiento: {asiento}\n")
        archivo.write(f"Pelicula: {pelicula}\n")
        archivo.write("----\n")
    print("Boucher Generado")










def cine_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            mostrar_peliculas()
        elif opcion == "2":
            mostrar_asientos()
        elif opcion == "3":
            comprar_entrada()
        elif opcion == "4":
           break
        else:
            print("Opcion invalida intente nuevamente")
cine_menu()











