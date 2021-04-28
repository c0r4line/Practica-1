#Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir aquellas que empiecen y terminen con la misma letra.
palabra= input("ingrese palabras, el corte es fin ").lower()
cant_car= len(palabra)
while palabra != "fin":        
    if (palabra[0]) == (palabra[cant_car-1]):
        print(palabra)
    palabra= input("ingrese palabras, el corte es fin ").lower()