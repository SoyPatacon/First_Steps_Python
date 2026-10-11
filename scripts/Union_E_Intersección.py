a = []
b = []
union = []
interseccion = []

for i in range (0,7):
    a.append(int(input(f"Ingresa el número {i+1} del arreglo A: ")))

for i in range (0,7):
    b.append(int(input(f"Ingresa el número {i+1} del arreglo B: ")))

totalunion = 0

for i in range (0,7):
    encontrado = False
    for j in range (0,7):
        if a[i] == b[j]:
            encontrado = True
    if encontrado == False:
        union.append(a[i])
        totalunion += 1

for i in range (0,7):
    encontrado = False
    for j in range (0,totalunion):
        if b[i] == union[j]:
            encontrado = True
    if encontrado == False:
        union.append(b[i])
        totalunion += 1

totalinterseccion = 0

for i in range (0,7):
    encontrado = False
    for j in range (0,7):
        if a[i] == b[j]:
            encontrado = True
    if encontrado == True:
        yaesta = False
        for j in range (0, totalinterseccion):
            if a[i] == interseccion[j]:
                yaesta = True
        if yaesta == False:
            totalinterseccion += 1
            interseccion.append(a[i])

print ("")
print ("===== ARREGLO A =====")
for i in range (0,7):
    print (f"{a[i]}", end = " ")
print ("")
print ("")

print ("===== ARREGLO B =====")
for i in range (0,7):
    print (f"{b[i]}", end = " ")
print ("")
print ("")

print ("===== UNIÓN =====")
for i in range (0,totalunion):
    print (f"{union[i]}", end = " ")
print ("")
print ("")

print ("===== INTERSECCIÓN =====")
for i in range (0,totalinterseccion):
    print (f"{interseccion[i]}", end = " ")