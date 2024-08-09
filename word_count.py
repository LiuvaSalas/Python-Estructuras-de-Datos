#Importacion de bibliotecas
import sys

#Decimos al usuario que introduzca el nombre del archivo .txt a procesar
archivo = sys.argv[1]

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