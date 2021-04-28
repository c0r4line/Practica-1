texto='''
       python es el mejor lenguaje de programacion
       '''

cadena=input("ingrese una letra ")
texto= texto.split()
if cadena.isupper():
  cadena=cadena.lower()
if (cadena <"a" or cadena >"z"):
    print ("error, no es una letra")
else:
    for palabra in texto:
        if(palabra[0] == cadena[0]):
            print("Las palabras que empiezan con la letra ingresada son ", palabra)
