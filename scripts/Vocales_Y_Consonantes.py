palabra = input("\nIngrese una palabra: ")

palabra = palabra.lower()
long = len(palabra)
vocales = 0
consonantes = 0

for i in range(long):
    letra = palabra[i]
    if letra in ("a", "e", "i", "o", "u"):
        vocales += 1
    elif letra in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        print (f"El caracter {letra} no es un caracter válido")
    else:
        if letra != " ":
            consonantes += 1

print(f"\nLa palabra {palabra} tiene {vocales} vocales")
print(f"\nLa palabra {palabra} tiene {consonantes} consonantes\n")