def formatear_monto(monto):
    if monto is not None:
        # Convierte a cadena y elimina caracteres no numéricos
        monto_str = ''.join(c for c in str(monto) if c.isdigit())
        
        # Agrega el signo de peso al principio
        monto_formateado = '$'
        
        # Verifica si hay un punto decimal y divide la cadena en partes
        if '.' in monto_str:
            partes = monto_str.split('.')
            parte_decimal = '.' + partes[1]
            monto_str = partes[0]
        else:
            parte_decimal = ''
        
        # Formatea la parte entera
        parte_entera_formateada = ""
        for i, digito in enumerate(monto_str[::-1]):
            if i > 0 and i % 3 == 0:
                parte_entera_formateada = "." + parte_entera_formateada
            parte_entera_formateada = digito + parte_entera_formateada
        
        # Combina las partes formateadas
        monto_formateado += parte_entera_formateada + parte_decimal
        
        return monto_formateado
    return monto
