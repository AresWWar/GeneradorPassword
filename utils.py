def obtener_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("❌ Por favor ingresa un número entero válido mayor que 0.")

def obtener_opcion_booleana(mensaje):
    while True:
        opcion = input(mensaje).lower()
        if opcion in ['s', 'sí', 'si']:
            return True
        elif opcion in ['n', 'no']:
            return False
        else:
            print("❌ Responde con 's' o 'n'.")
