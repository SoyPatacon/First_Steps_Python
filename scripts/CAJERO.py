print ("===== CAJERO PERRON =====\n")

saldo_max = 2000000
max_consig = 500000
saldo = 0
opcion = 0

while opcion != 4:

    print ("1 = Saldo")
    print ("2 = Consignar")
    print ("3 = Retirar")
    print ("4 = Salir")
    opcion = int(input("\nIngrese la opción de la operación que desea realizar: "))

    if opcion == 1:
        if saldo >= 0:
            print(f"Su saldo es ${saldo:,.2f}".replace(",", "."))
        else:
            print("Su saldo es negativo.")
        seguir = input("\n¿Desea hacer otra operación?: (Si / No): ").lower().strip()
        if seguir == "si":
            print("")
            continue
        else:
            opcion = 4
            print ("GRACIAS POR USAR EL CAJERO PERRON")

    elif opcion == 2:
        if saldo < saldo_max:
            valor_consig = float(input("\nIngrese el monto a consignar: "))
            if valor_consig > max_consig:
                print("El monto máximo para consignar es de $500.000")
            if valor_consig <= max_consig and saldo + valor_consig <= saldo_max and valor_consig > 0:
                saldo += valor_consig
            seguir = input("\n¿Desea hacer otra operación?: (Si / No): ").lower().strip()
            if seguir == "si":
                print("")
                continue
            else:
                opcion = 4
                print ("GRACIAS POR USAR EL CAJERO PERRON")
        else:
            print ("Ya has llegado al saldo máximo de $2.000.000\n")

    elif opcion == 3:
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro > 0 and saldo > 0:
            saldo -= retiro
        else:
            print("Ingrese una cantidad valida para retirar.")
        seguir = input("\n¿Desea hacer otra operación?: (Si / No): ").lower().strip()
        if seguir == "si":
            print ("")
            continue
        else:
            opcion = 4
            print ("GRACIAS POR USAR EL CAJERO PERRON")

    elif opcion == 4:
        print ("GRACIAS POR USAR EL CAJERO PERRON")
    
    else:
        print ("\nOpción no válida.\n")