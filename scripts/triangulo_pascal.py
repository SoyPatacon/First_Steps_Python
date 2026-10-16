"""
Triángulo de Pascal: 4 algoritmos distintos.

Cada algoritmo devuelve una lista de filas (lista de listas de enteros).
La función mostrar() las imprime centradas en la consola.
"""

from functools import lru_cache
from math import factorial


# ---------------------------------------------------------------------------
# ALGORITMO 1: Iterativo (cada fila se construye sumando la fila anterior)
# Complejidad: O(n^2) tiempo, O(n^2) memoria (guardando todas las filas)
# ---------------------------------------------------------------------------
def pascal_iterativo(n):
    triangulo = []
    for i in range(n):
        fila = [1] * (i + 1)                  # los extremos siempre son 1
        for j in range(1, i):                 # los de en medio se suman
            fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        triangulo.append(fila)
    return triangulo


# ---------------------------------------------------------------------------
# ALGORITMO 2: Recursivo con memoización
# C(f, c) = C(f-1, c-1) + C(f-1, c), con C(f, 0) = C(f, f) = 1
# lru_cache evita recalcular los mismos valores (sin él sería exponencial).
# ---------------------------------------------------------------------------
@lru_cache(maxsize=None)
def combinacion_recursiva(fila, col):
    if col == 0 or col == fila:
        return 1
    return combinacion_recursiva(fila - 1, col - 1) + combinacion_recursiva(fila - 1, col)


def pascal_recursivo(n):
    return [[combinacion_recursiva(f, c) for c in range(f + 1)] for f in range(n)]


# ---------------------------------------------------------------------------
# ALGORITMO 3: Fórmula con factoriales (coeficiente binomial)
# C(n, k) = n! / (k! * (n - k)!)
# ---------------------------------------------------------------------------
def pascal_factorial(n):
    return [
        [factorial(f) // (factorial(c) * factorial(f - c)) for c in range(f + 1)]
        for f in range(n)
    ]


# ---------------------------------------------------------------------------
# ALGORITMO 4: Fórmula multiplicativa (cada elemento sale del anterior)
# C(n, k+1) = C(n, k) * (n - k) / (k + 1)
# No usa factoriales grandes ni la fila anterior: solo el elemento previo.
# ---------------------------------------------------------------------------
def pascal_multiplicativo(n):
    triangulo = []
    for f in range(n):
        fila = [1]
        for k in range(f):
            fila.append(fila[k] * (f - k) // (k + 1))
        triangulo.append(fila)
    return triangulo


# ---------------------------------------------------------------------------
# Impresión en consola (triángulo centrado)
# ---------------------------------------------------------------------------
def mostrar(triangulo, titulo):
    print(f"\n=== {titulo} ===")
    # El ancho de la última fila sirve para centrar todas las demás
    ancho = len(" ".join(map(str, triangulo[-1])))
    for fila in triangulo:
        print(" ".join(map(str, fila)).center(ancho))


if __name__ == "__main__":
    try:
        n = int(input("¿Cuántas filas quieres? (por defecto 8): ") or 8)
    except ValueError:
        n = 8

    if n < 1:
        print("El número de filas debe ser al menos 1.")
    else:
        algoritmos = [
            (pascal_iterativo, "1) Iterativo (suma de la fila anterior)"),
            (pascal_recursivo, "2) Recursivo con memoización"),
            (pascal_factorial, "3) Fórmula con factoriales"),
            (pascal_multiplicativo, "4) Fórmula multiplicativa"),
        ]

        resultados = []
        for funcion, titulo in algoritmos:
            tri = funcion(n)
            resultados.append(tri)
            mostrar(tri, titulo)

        # Verificación: los 4 métodos deben dar exactamente lo mismo
        coinciden = all(r == resultados[0] for r in resultados)
        print("\nLos 4 algoritmos coinciden:", "SÍ" if coinciden else "NO")
