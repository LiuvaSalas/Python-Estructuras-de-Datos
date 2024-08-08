#Decimos al usuario que introduzca el nombre del archivo .txt a procesar
archivo = input("Ingresa el nombre del archivo de texto incluyendo su extensión '.txt', ejemplo; texto.txt: ")


try:
    with open(archivo, "r") as file:
        texto = file.read()
        #Contamos las palabras y las letras despues de introducirlas dentro de un set para unificarlas
        palabras = len(set(texto.split()))
        letras = len(set(texto))
        print(f"El número de caracteres distintos es: {letras}")
        print(f"El número de palabras distintas es: {palabras}")
except IndexError:
    print("Por favor, ingrese el nombre de un archivo .txt.")