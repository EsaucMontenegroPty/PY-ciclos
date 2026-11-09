palabra = input("Ingrese la palabra para salir: ")

while palabra != "salir":
    print("Opcion no valida")
    palabra = input("Ingrese la palabra para salir: ")  

    if palabra == "salir":
        print("Hasta luego!")