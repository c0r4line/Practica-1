#escribir una función que imprima sus argumentos agregando de qué tipo son.

def imprimo(*args):
    """ Esta función imprime los argumentos y sus tipos"""
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")

imprimo(1)
print("-"*30)
imprimo(2, "hola")
print("-"*30)
imprimo([1,2], "hola", 3.2)