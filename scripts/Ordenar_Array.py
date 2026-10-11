numeros = []
print ("")

for i in range (1, 6):
    numeros.append(int(input(f"Ingrese el numero {i}: ")))

for i in range (0, 5):
    for j in range (0, 5):
        if numeros[i] < numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print (f"\nLa lista ordenada es: {numeros}.\n".center(30, "="))


