from generator import generar_contraseña
from utils import obtener_opcion_booleana, obtener_entero

def main():
    print("🔐 GENERADOR DE CONTRASEÑAS PERSONALIZADO 🔐")
    
    longitud = obtener_entero("Longitud de la contraseña: ")
    
    print("\nTipo de contraseña:")
    print("1. Solo números")
    print("2. Solo letras")
    print("3. Alfanumérica")
    
    while True:
        tipo = input("Selecciona el tipo (1/2/3): ")
        if tipo in ["1", "2", "3"]:
            break
        else:
            print("❌ Selección inválida. Debe ser 1, 2 o 3.")

    incluir_numeros = False
    incluir_simbolos = False
    incluir_minusculas = False
    incluir_mayusculas = False

    if tipo == "1":
        incluir_numeros = True

    elif tipo == "2":
        incluir_minusculas = obtener_opcion_booleana("¿Incluir letras minúsculas? (s/n): ")
        incluir_mayusculas = obtener_opcion_booleana("¿Incluir letras mayúsculas? (s/n): ")

    elif tipo == "3":
        incluir_numeros = obtener_opcion_booleana("¿Incluir números? (s/n): ")
        incluir_simbolos = obtener_opcion_booleana("¿Incluir símbolos? (s/n): ")
        incluir_minusculas = obtener_opcion_booleana("¿Incluir letras minúsculas? (s/n): ")
        incluir_mayusculas = obtener_opcion_booleana("¿Incluir letras mayúsculas? (s/n): ")

    try:
        contraseña = generar_contraseña(
            longitud=int(longitud),
            incluir_numeros=incluir_numeros,
            incluir_simbolos=incluir_simbolos,
            incluir_minusculas=incluir_minusculas,
            incluir_mayusculas=incluir_mayusculas
        )
        print(f"\n✅ Contraseña generada: {contraseña}")
    except ValueError as e:
        print(f"\n❌ No se puede generar la contraseña: {e}")

if __name__ == "__main__":
    main()
