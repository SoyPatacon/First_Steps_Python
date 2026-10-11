def serie_ln(x):
    """ln(x) por serie, funciona bien para x cercano a 1."""
    z = (x - 1) / (x + 1)
    z2 = z * z
    termino = z
    suma = 0.0
    n = 1
    while abs(termino) / n > 1e-16:
        suma += termino / n
        termino *= z2
        n += 2
    return 2 * suma

LN2 = serie_ln(2) 

def ln(x):
    """Logaritmo natural sin librerías."""
    if x <= 0:
        raise ValueError("El número debe ser mayor que 0")
    k = 0
    while x > 1.5:   
        x /= 2
        k += 1
    while x < 0.75:
        x *= 2
        k -= 1
    return serie_ln(x) + k * LN2

def logaritmo(numero, base):
    if numero <= 0:
        raise ValueError("El número debe ser mayor que 0")
    if base <= 0 or base == 1:
        raise ValueError("La base debe ser mayor que 0 y distinta de 1")
    return ln(numero) / ln(base)


print("\n ===== CALCULADORA PERRONA =====")

while True:
    print("\nOpciones:")
    print("1. Raíz")
    print("2. Potencia")
    print("3. Logaritmo")

    opcion = input("Selecciona una opción (1, 2, 3) o 'salir' para terminar: ").lower()

    if opcion == "salir":
        print("¡Hasta luego!")
        break
    elif opcion == "1":
        numero = float(input("Ingresa el número para calcular la raíz: "))
        numero2 = float(input("Ingresa el índice de la raíz: "))
        resultado = numero ** (1 / numero2)
        print(f"La raíz {numero2} de {numero} es: {resultado}")
    elif opcion == "2":
        base = float(input("Ingresa la base: "))
        exponente = float(input("Ingresa el exponente: "))
        resultado = base ** exponente
        print(f"{base} elevado a {exponente} es: {resultado}")
    elif opcion == "3":
        numero = float(input("Ingresa el número: "))
        base = float(input("Ingresa la base del logaritmo: "))
        try:
            resultado = logaritmo(numero, base)
            print(f"El logaritmo base {base} de {numero} es: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Opción no válida.")
