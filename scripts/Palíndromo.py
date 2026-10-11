palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()

for i in range (len(palabra)):
    if palabra[i] != palabra[len(palabra)-1-i]:
        print(f"\nLa palabra {palabra} no es un palíndromo")
        break
else:
    print(f"\nLa palabra {palabra} es un palíndromo")