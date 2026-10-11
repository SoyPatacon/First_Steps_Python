print ("===== TIENDA PERRONA =====\n")

edad = int(input("Ingresa tu edad: "))
compra = float(input("Ingresa el precio total de tu compra: "))

if edad >= 65 or compra >= 300000:
    descuento = compra * 0.15
    precio_final = compra - descuento
    print(f"\n¡Opaa! Tienes un descuento del 15%.\nPrecio final: ${precio_final:.2f}\n")
else:
    print(f"\nNo cumples con los requisitos para obtener un descuento.\nPrecio final: ${compra:.2f}\n")