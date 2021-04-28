
frase= input('Ingrese una frase o palabra ')

#ord: recibe un caracter y regresa un entero que lo representa porej @ = 64, asi puedo comprobar si es una letra

frase = [ x for x in frase if ( ord(x) >= ord('a') and ord(x) <= ord('z') )]   

#un conjunto(set) contiene valores únicos, si la longitud del conjunto es igual al número de ocurrencias en len de frase significa que ocurrió una vez
  
if(len(set(frase)) == len(frase)):
    print('es un heterograma')
else:
    print('no es un heterograma')

     
     
     
  
     
     
  