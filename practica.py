
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def mostrar_menu():
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresa un número válido.")


def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("Saliendo de la calculadora")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida")
            continue

        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        if opcion == "4":
            while num2 == 0:
                print("No se puede dividir entre 0")
                num2 = pedir_numero("Ingresa otro número distinto de 0: ")

        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calculadora()

