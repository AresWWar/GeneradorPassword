# Importa el módulo random para selección aleatoria de caracteres
import random

# Importa el módulo string que contiene constantes como dígitos, letras, símbolos, etc.
import string

# Función que genera una contraseña segura según los parámetros indicados por el usuario
def generar_contraseña(longitud, incluir_numeros, incluir_simbolos, incluir_minusculas, incluir_mayusculas):
    
    # Valida que la longitud solicitada sea mayor que cero
    if longitud < 1:
        raise ValueError("La longitud debe ser mayor que cero.")

    caracteres_disponibles = ""  # Cadena que almacenará todos los caracteres válidos posibles
    obligatorios = []            # Lista para asegurar que al menos un carácter de cada tipo requerido esté presente

    # Si el usuario desea incluir números
    if incluir_numeros:
        caracteres_disponibles += string.digits  # Agrega los dígitos 0-9 a los caracteres disponibles
        obligatorios.append(random.choice(string.digits))  # Garantiza al menos un número

    # Si desea incluir letras minúsculas
    if incluir_minusculas:
        caracteres_disponibles += string.ascii_lowercase  # Agrega a-z
        obligatorios.append(random.choice(string.ascii_lowercase))  # Garantiza una minúscula

    # Si desea incluir letras mayúsculas
    if incluir_mayusculas:
        caracteres_disponibles += string.ascii_uppercase  # Agrega A-Z
        obligatorios.append(random.choice(string.ascii_uppercase))  # Garantiza una mayúscula

    # Si desea incluir símbolos
    if incluir_simbolos:
        caracteres_disponibles += string.punctuation  # Agrega símbolos como !@#$%^&*()
        obligatorios.append(random.choice(string.punctuation))  # Garantiza un símbolo

    # Verifica que al menos se haya seleccionado un tipo de carácter
    if not caracteres_disponibles:
        raise ValueError(" ⚠️ No se seleccionaron tipos de caracteres válidos.")

    # Verifica que la longitud sea suficiente para contener todos los obligatorios
    if longitud < len(obligatorios):
        raise ValueError(f"La longitud debe ser al menos {len(obligatorios)} para cumplir con los requisitos seleccionados.")

    # Genera el resto de la contraseña con caracteres aleatorios del conjunto permitido
    restantes = [random.choice(caracteres_disponibles) for _ in range(longitud - len(obligatorios))]

    # Combina los caracteres obligatorios con los restantes
    contraseña = obligatorios + restantes

    # Mezcla el orden de todos los caracteres para mayor aleatoriedad
    random.shuffle(contraseña)

    # Retorna la contraseña como una cadena unificada
    return ''.join(contraseña)
