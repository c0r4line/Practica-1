def valores(letra):
    cant = 0
    if((letra >= "A") or (letra <= "Z")):
        if letra in ('A, E, I, O, U, L, N, R, S, T'):
            cant += 1
        elif letra in ('D,G'):
            cant += 2
        elif letra in ('B,C,M,P'):
            cant += 3
        elif letra in ('F,H,V,W,Y'):
            cant += 4
        elif letra in ('K'):
            cant += 5
        elif letra in ('J,X'):
            cant += 8
        elif letra in ('Q,Z'):
            cant += 10
    return cant
# otra forma VER, arreglar xq no suma los puntajes!!!
#puntajes = {('a','b','c','d'): 1 , ('h','o'): 2, ('l',): 3}
#palabra = 'hola'

# for letra in palabra:
#    for letras, puntaje in puntajes.items():
#        if letra in letras:
#            print(f"{letra}: {puntaje}")


cadena = input("ingrese una palabra ").upper()
cantidad = 0
for letra in cadena:
    cantidad += valores(letra)
if(cantidad == 0):
    print("no ingreso ninguna palabra")
else:
    print("el valor de la palabra ingresada es : ")
    print(cantidad)
