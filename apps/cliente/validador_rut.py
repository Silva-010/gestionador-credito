def validar_rut_chileno(rut):
    """
    Valida si un RUT chileno es válido.
    :param rut: El RUT a validar en formato "12345678-9" o "12.345.678-9".
    :return: True si el RUT es válido, False en caso contrario.
    """
    # Elimina puntos y guiones del RUT y lo divide en número y dígito verificador
    rut = rut.replace(".", "").replace("-", "")
    if not rut[:-1].isdigit() or (not rut[-1].isdigit() and rut[-1] != 'k' and rut[-1] != 'K'):
        return False

    numero, verificador = rut[:-1], rut[-1].upper()

    # Calcula el dígito verificador esperado
    suma = 0
    multiplicador = 2

    for d in reversed(numero):
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    digito_esperado = 11 - resto if resto != 0 else 0

    # Maneja el caso especial del dígito "K"
    if digito_esperado == 10:
        digito_esperado = 'K'

    # Compara el dígito verificador calculado con el proporcionado (en mayúsculas)
    return verificador == str(digito_esperado).upper()

def formatear_rut(rut):
    # Elimina puntos y guiones del RUT
    rut = rut.replace(".", "").replace("-", "")
    
    # Divide en número y dígito verificador
    numero, verificador = rut[:-1], rut[-1].upper()

    # Formatea el RUT en el formato deseado
    rut_formateado = ""
    for i, digito in enumerate(numero[::-1]):
        if i > 0 and i % 3 == 0:
            rut_formateado = "." + rut_formateado
        rut_formateado = digito + rut_formateado

    rut_formateado = rut_formateado + "-" + verificador

    return rut_formateado

