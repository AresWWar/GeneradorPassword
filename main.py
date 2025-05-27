# Importamos la función principal que genera la contraseña
from generator import generar_contraseña

# Importamos funciones auxiliares para entrada del usuario
from utils import obtener_opcion_booleana, obtener_entero

# Función principal del programa
def main():

    # Muestra un encabezado en consola
    print("🔐 GENERADOR DE CONTRASEÑAS PERSONALIZADO 🔐")

    # Solicita al usuario la longitud deseada para la contraseña
    longitud = obtener_entero("Longitud de la contraseña: ")

    # Muestra las opciones de tipo de contraseña que se pueden generar
    print("\nTipo de contraseña:")
    print("1. Solo números")
    print("2. Solo letras")
    print("3. Alfanumérica")
    
    # Ciclo para asegurar una selección válida del tipo de contraseña
    while True:
        tipo = input("Selecciona el tipo (1/2/3): ")
        if tipo in ["1", "2", "3"]:
            break
        else:
            print("❌ Selección inválida. Debe ser 1, 2 o 3.")

    # Inicializa las variables que definen los tipos de caracteres permitidos
    incluir_numeros = False
    incluir_simbolos = False
    incluir_minusculas = False
    incluir_mayusculas = False

    # Si el tipo elegido es solo números, se activan solo los números
    if tipo == "1":
        incluir_numeros = True

    # Si se elige solo letras, se pregunta si incluir minúsculas y/o mayúsculas
    elif tipo == "2":
        incluir_minusculas = obtener_opcion_booleana("¿Incluir letras minúsculas? (s/n): ")
        incluir_mayusculas = obtener_opcion_booleana("¿Incluir letras mayúsculas? (s/n): ")

    # Si se elige alfanumérica, se pregunta si incluir cada tipo: números, símbolos, letras minúsculas y mayúsculas
    elif tipo == "3":
        incluir_numeros = obtener_opcion_booleana("¿Incluir números? (s/n): ")
        incluir_simbolos = obtener_opcion_booleana("¿Incluir símbolos? (s/n): ")
        incluir_minusculas = obtener_opcion_booleana("¿Incluir letras minúsculas? (s/n): ")
        incluir_mayusculas = obtener_opcion_booleana("¿Incluir letras mayúsculas? (s/n): ")

    try:
        # Se genera la contraseña con los parámetros seleccionados por el usuario
        contraseña = generar_contraseña(
            longitud=int(longitud),
            incluir_numeros=incluir_numeros,
            incluir_simbolos=incluir_simbolos,
            incluir_minusculas=incluir_minusculas,
            incluir_mayusculas=incluir_mayusculas
        )
        # Muestra la contraseña generada si no hubo errores
        print(f"\n✅ Contraseña generada: {contraseña}")
    except ValueError as e:
        # Captura errores como: longitud insuficiente o falta de tipos seleccionados
        print(f"\n❌ No se puede generar la contraseña: {e}")

if __name__ == "__main__":
    main()
