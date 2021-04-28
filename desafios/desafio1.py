#Escribir un programa que ingrese 4 palabras desde el teclado e imprima aquellas que contienen la letra “r”.



for i in range(4):
    cadena= input("ingrese 4 palabras: ")
    mensaje= "Tiene r" if "r" in cadena else "No tiene r"
    print(mensaje)