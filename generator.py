import random
import string

def generar_contraseña(longitud, incluir_numeros, incluir_simbolos, incluir_minusculas, incluir_mayusculas):
    if longitud < 1:
        raise ValueError("La longitud debe ser mayor que cero.")

    caracteres_disponibles = ""
    obligatorios = []

    # Números
    if incluir_numeros:
        caracteres_disponibles += string.digits
        obligatorios.append(random.choice(string.digits))

    # Letras
    if incluir_minusculas:
        caracteres_disponibles += string.ascii_lowercase
        obligatorios.append(random.choice(string.ascii_lowercase))

    if incluir_mayusculas:
        caracteres_disponibles += string.ascii_uppercase
        obligatorios.append(random.choice(string.ascii_uppercase))

    # Símbolos
    if incluir_simbolos:
        caracteres_disponibles += string.punctuation
        obligatorios.append(random.choice(string.punctuation))

    if not caracteres_disponibles:
        raise ValueError("⚠️ No se seleccionaron tipos de caracteres válidos.")

    if longitud < len(obligatorios):
        raise ValueError(f"La longitud debe ser al menos {len(obligatorios)} para cumplir con los requisitos seleccionados.")

    # Relleno
    restantes = [random.choice(caracteres_disponibles) for _ in range(longitud - len(obligatorios))]

    # Mezcla y retorna
    contraseña = obligatorios + restantes
    random.shuffle(contraseña)
    return ''.join(contraseña)
