try:
    n = int(input("Ingresa la cantidad de filas para el triángulo de Pascal: "))
    if n > 0:
        for i in range(n):
            print(" " * (n - i), end = "")
            coeficiente = 1
            for j in range(1, i + 2):
                print(coeficiente, end = " ")
                coeficiente = coeficiente * (i - j + 1) // j
            print("")
    else:
        print("Por favor ingresa un número mayor a 0")
except ValueError:
    print("Entrada no válida, debe ingresar un número entero.")