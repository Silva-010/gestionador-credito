def validar_telefono_chileno(telefono):
    """
    Valida un número de teléfono con formato chileno.

    Args:
        telefono: El número de teléfono a validar.

    Returns:
        True si el número es válido, False si no lo es.
    """

    # Elimina los espacios en blanco del número de teléfono
    telefono = telefono.strip()

    # El número debe comenzar con +56
    if not telefono.startswith("+56"):
        return False

    # El número debe tener 9 dígitos después del +56
    if len(telefono[3:]) != 9:
        return False

    # Los dígitos deben ser números del 0 al 9
    for digito in telefono[3:]:
        if not digito.isdigit():
            return False

    return True

def formatear_telefono_chileno(telefono):

    # Elimina los espacios en blanco del número de teléfono
    telefono = telefono.strip()

    # Verifica que el número de teléfono tenga al menos 11 caracteres (incluyendo el "+56" y los dígitos)
    if len(telefono) < 11:
        # El número no tiene la longitud mínima, no es válido
        return None  # O puedes lanzar una excepción si lo prefieres

    # Agrega el prefijo "+56" al número de teléfono
    telefono_formateado = "+56" + telefono[3:]

    return telefono_formateado