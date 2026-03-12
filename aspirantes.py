# Sprint 1: Registro Inicial

# Bienvenida al aspirante

print("Bienvenido al programa de selección de aspirantes.")
personas = int(input("¿Cuántas personas desean participar?: "))

for i in range(personas):
    print(f"\nRegistro del aspirante #{i + 1}")
    name = input("Por favor, ingrese su nombre y primer apellido: ")

    while True:
        edad_input = input("Ingrese su edad: ")

        if not edad_input.isdigit():
            print("Error: Ingrese una edad válida.")
            continue

        edad = int(edad_input)

        if edad <= 0:
            print("Error: La edad no es válida.")
            continue

        break

    conocimientos = input("¿Tienes conocimientos básicos en computación? (si/no): ").lower()

    if edad >= 15 and conocimientos == "si":
        print("Puede participar en el programa")
    else:
        print("No cumples con los requisitos")

print("\nProceso Terminado")