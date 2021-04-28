#implementar una función que dada una cadena de texto, retorne las palabras que contiene en orden alfabético.

def ordeno1(cadena):
    """ Implementación usando sort"""
    lista = cadena.split()
    #lista.sort(key=str.lower)
    lista.sort()
    return lista
print(ordeno1("Hoy puede ser un gran día. "))

# Otra posible solución
def ordeno2(cadena):
    """ Implementación usando sorted"""
    lista = cadena.split()
    return sorted(lista, key=str.lower)
print(ordeno2("Hoy puede ser un gran día. "))