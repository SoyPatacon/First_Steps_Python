n = int(input("Ingrese su numero: "))

esprimo = True

if n < 2:
    esprimo = False
else:
    i = 2
    while i ** 2 <= n and esprimo == True:
        if n % i == 0:
            esprimo = False
        i += 1

if esprimo == True:
    print (f"\n{n} es primo\n")
else:
    print (f"\n{n} no es primo\n")