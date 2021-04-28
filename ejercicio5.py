texto = input("ingrese una frase" )
palab= input("ingrese una palabra a buscar en la frase")
texto = texto.lower()
palab = palab.lower()
texto= texto.split(" ")
cont=0
for palabra in texto:
    if palabra == palab:
        cont+=1
print("la palabra ingresada aparece " , cont)