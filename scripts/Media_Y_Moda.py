notas = []

frecmax, freactual = 0, 0
moda = 0

n = int(input("¿Cuántas notas vas a evaluar? "))

for i in range (0, n):
    nota = float(input(f"Ingresa la nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print ("")
print("===== MEDIA DE NOTAS =====")
print(f"La media es: {media}")

for i in range (0, n):
    frecactual = 0
    for j in range (0, n):
        if notas[i] == notas[j]:
            frecactual += 1
    if frecactual > frecmax:
        frecmax = frecactual
        moda = notas[i]

if frecmax > 1:
    print("===== MODA DE NOTAS =====")
    print(f"La moda es: {moda}")
    print ("")
elif frecmax == 1:
    print("===== MODA DE NOTAS =====")
    print("No hay moda, todas las notas son diferentes")
    print ("")

