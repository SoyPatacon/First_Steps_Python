"""
Ejercicios de matemática básica (8° y 9°) resueltos en Python.
Parte 1: los 6 ejercicios pedidos.
Parte 2: ejercicios aplicados al álgebra.
"""
import math

# ======================================================================
# PARTE 1: LOS SEIS EJERCICIOS
# ======================================================================

# 1. Hipotenusa con Pitágoras: c = raíz(a² + b²)
def hipotenusa(a, b):
    return math.sqrt(a**2 + b**2)

# 2. Área de un círculo: A = π r²
def area_circulo(radio):
    return math.pi * radio**2

# 3. Media de una lista de notas
def media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# 4. Par, primo, divisible
def es_par(n):
    return n % 2 == 0

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def es_divisible(a, b):
    """True si a es divisible por b."""
    return b != 0 and a % b == 0

# 5. MCD con el algoritmo de Euclides
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

# 6. Tabla de valores de f(x) = 2x + 3
def f(x):
    return 2 * x + 3

def tabla_f():
    print("  x |  f(x)")
    print("----+------")
    for x in range(0, 11):
        print(f"{x:3} | {f(x):4}")


# ======================================================================
# PARTE 2: EJERCICIOS APLICADOS AL ÁLGEBRA
# ======================================================================

# A. Ecuación lineal ax + b = c  ->  x = (c - b) / a
def resolver_lineal(a, b, c):
    if a == 0:
        return "Sin solución" if b != c else "Infinitas soluciones"
    return (c - b) / a

# B. Ecuación cuadrática ax² + bx + c = 0
def resolver_cuadratica(a, b, c):
    if a == 0:
        return resolver_lineal(b, 0, -c)
    d = b**2 - 4*a*c            # discriminante
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        return (-b / (2*a),)
    else:
        return None             # no hay soluciones reales

# C. Sistema 2x2 por regla de Cramer
#    a1 x + b1 y = c1
#    a2 x + b2 y = c2
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    det = a1*b2 - a2*b1
    if det == 0:
        return None             # sin solución única
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    return x, y

# D. Evaluar un polinomio (coeficientes de mayor a menor grado)
#    [2, -3, 1] representa 2x² - 3x + 1
def evaluar_polinomio(coef, x):
    resultado = 0
    for c in coef:              # método de Horner
        resultado = resultado * x + c
    return resultado

# E. Suma de polinomios
def sumar_polinomios(p, q):
    n = max(len(p), len(q))
    p = [0] * (n - len(p)) + p  # alinear por el grado menor
    q = [0] * (n - len(q)) + q
    return [a + b for a, b in zip(p, q)]

# F. Multiplicación de polinomios
def multiplicar_polinomios(p, q):
    resultado = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            resultado[i + j] += a * b
    return resultado

# G. Mostrar un polinomio como texto
def polinomio_a_texto(coef):
    grado = len(coef) - 1
    terminos = []
    for i, c in enumerate(coef):
        if c == 0:
            continue
        exp = grado - i
        if exp == 0:
            terminos.append(f"{c}")
        elif exp == 1:
            terminos.append(f"{c}x")
        else:
            terminos.append(f"{c}x^{exp}")
    return " + ".join(terminos).replace("+ -", "- ") if terminos else "0"

# H. Pendiente y ecuación de la recta que pasa por dos puntos
def recta_dos_puntos(x1, y1, x2, y2):
    if x1 == x2:
        return f"Recta vertical: x = {x1}"
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b                 # y = mx + b

# I. Distancia y punto medio entre dos puntos
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def punto_medio(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

# J. Verificar el producto notable (a + b)² = a² + 2ab + b²
def verificar_binomio_cuadrado(a, b):
    izquierda = (a + b)**2
    derecha = a**2 + 2*a*b + b**2
    return izquierda == derecha

# K. Factorizar x² + bx + c = (x + p)(x + q) buscando p + q = b y p*q = c
def factorizar_trinomio(b, c):
    for p in range(-abs(c) - 1, abs(c) + 2):
        for q in range(-abs(c) - 1, abs(c) + 2):
            if p + q == b and p * q == c:
                return p, q
    return None

# L. Despeje de fórmulas: v = d / t
def despejar_distancia(v, t):
    return v * t

def despejar_tiempo(d, v):
    return d / v

# M. Problema aplicado: dos números suman S y su producto es P.
#    Son las raíces de x² - Sx + P = 0.
def dos_numeros(suma, producto):
    return resolver_cuadratica(1, -suma, producto)


# ======================================================================
# PRUEBAS
# ======================================================================
if __name__ == "__main__":
    print("=== PARTE 1 ===")
    print("Hipotenusa (3, 4):", hipotenusa(3, 4))                  # 5.0
    print("Área círculo r=5:", round(area_circulo(5), 2))          # 78.54
    print("Media [4.5, 3.8, 5.0, 4.2]:", media([4.5, 3.8, 5.0, 4.2]))
    print("¿12 es par?", es_par(12))
    print("¿17 es primo?", es_primo(17))
    print("¿20 divisible por 5?", es_divisible(20, 5))
    print("MCD(48, 18):", mcd(48, 18))                             # 6
    print("MCM(48, 18):", mcm(48, 18))                             # 144
    tabla_f()

    print("\n=== PARTE 2 ===")
    print("2x + 3 = 11 ->  x =", resolver_lineal(2, 3, 11))        # 4.0
    print("x² - 5x + 6 = 0 ->", resolver_cuadratica(1, -5, 6))     # (3.0, 2.0)
    print("Sistema x+y=10, x-y=2 ->", resolver_sistema(1, 1, 10, 1, -1, 2))
    print("P(x)=2x²-3x+1, P(2) =", evaluar_polinomio([2, -3, 1], 2))
    p, q = [1, 2], [1, -2]       # (x + 2) y (x - 2)
    print("Suma:", polinomio_a_texto(sumar_polinomios(p, q)))
    print("Producto:", polinomio_a_texto(multiplicar_polinomios(p, q)))
    print("Recta por (1,2) y (3,8): m, b =", recta_dos_puntos(1, 2, 3, 8))
    print("Distancia (0,0)-(3,4):", distancia(0, 0, 3, 4))
    print("Punto medio (0,0)-(4,6):", punto_medio(0, 0, 4, 6))
    print("(a+b)² verificado:", verificar_binomio_cuadrado(3, 5))
    print("x² + 5x + 6 = (x + p)(x + q):", factorizar_trinomio(5, 6))
    print("Distancia a 60 km/h durante 2.5 h:", despejar_distancia(60, 2.5))
    print("Dos números que suman 10 y multiplican 21:", dos_numeros(10, 21))

    # Ejercicios propuestos para practicar (sin solución aquí):
    # 1. Resolver 5x - 7 = 3x + 9 (pista: llévalo a la forma ax + b = c).
    # 2. Hallar dos números consecutivos cuya suma sea 51.
    # 3. Resolver 2x² - 8x + 6 = 0 y verificar las raíces evaluando el polinomio.
    # 4. Escribir una función que reciba una lista de coeficientes y diga
    #    si el polinomio tiene la raíz x = 1.