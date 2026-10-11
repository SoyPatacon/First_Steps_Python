import math


print ("\n ===== PLANO CARTESIANO UWU =====\n")
x1 = float(input("\nQué valor tomará x1: "))
y1 = float(input("Qué valor tomará y1: "))
x2 = float(input("Qué valor tomará x2: "))
y2 = float(input("Qué valor tomará y2: "))

D = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

R = (x1 + x2, y1 + y2)

print ("\n ===== RESULTADOS =====")

if x2 - x1 == 0:
    print("\nDividiste entre cero (x1 = x2), la recta es vertical.")
    print(f"Pendiente (m) = No definida")
    print(f"Ecuación de recta: x = {x1}")
else:
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    print(f"\nPendiente (m) = {m:.2f}")
    print(f"Intersección (b) = {b:.2f}")
    print(f"Ecuación de la recta: y = {m:.2f}x + {b:.2f}")

print(f"Distancia entre puntos (D) = {D:.2f}")
print(f"Resultado (R) = {R:.2f}\n")