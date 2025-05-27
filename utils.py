# Esta función solicita al usuario un número entero positivo desde consola
def obtener_entero(mensaje):
    while True:
        try:
            # Se intenta convertir la entrada del usuario a entero
            valor = int(input(mensaje))

            # Se verifica que el número sea mayor que 0
            if valor <= 0:
                raise ValueError  # Lanza una excepción si es menor o igual a cero

            return valor  # Devuelve el valor válido
        except ValueError:
            # Si ocurre un error en la conversión o es un número inválido, se muestra un mensaje de error
            print("❌ Por favor ingresa un número entero válido mayor que 0.")

# Esta función solicita al usuario una respuesta afirmativa o negativa ('s' o 'n'),
# y devuelve un valor booleano True o False según la respuesta.
def obtener_opcion_booleana(mensaje):
    while True:
        # Se solicita la respuesta y se convierte a minúsculas para facilitar la comparación
        opcion = input(mensaje).lower()

        # Se evalúan formas válidas de respuesta afirmativa
        if opcion in ['s', 'sí', 'si']:
            return True

        # Se evalúan formas válidas de respuesta negativa
        elif opcion in ['n', 'no']:
            return False

        # Si la respuesta no es válida, se muestra un mensaje de error y se repite
        else:
            print("❌ Responde con 's' o 'n'.")
