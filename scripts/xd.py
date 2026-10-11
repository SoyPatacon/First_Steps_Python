# EJERCICIO a.)
for numeros in range (1,20):
    if numeros % 7 == 0:
        break
print (" ")
print (numeros)

#EJERCICIO b.)
for multiplos in range (1, 15):
    if multiplos % 3 == 0:
        continue
    print (multiplos, end = " ")

#EJERCICIO 2
print ("")
dato = "    correo@ejemplo.com   \n"
print (dato.strip(" \n "))

#EJERCICIO 3 (resultado = pYTHON es GENIAl)
print ("Python ES genial".swapcase())

#EJERCICIO 4
libro = "cien años de soledad"
print (libro.title())


#EJERCICIO 5 
nombres = ["ana", "MARIO", "sofía"]
for nombre in nombres:
    print (nombre.capitalize(), end = " ")
print ("")

#EJERCICIO 6
compras = []
for i in range (0,2):
    compras.append("pan")
    compras.append("leche")
    compras.append("huevos")
    break
print (compras)

#EJERCICIO COMBINADO (me podrías explicar como se realiza? Necesito mejorar mi comprension en cuanto a listas y arrays)

palabras = ["  hola  ", "MUNDO", "Python  "]
resultado = []

for palabra in palabras:
    limpia = palabra.strip()
    formateada = limpia.title()
    resultado.append(formateada)

print (resultado)