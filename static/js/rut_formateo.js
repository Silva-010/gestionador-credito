// Función para formatear el RUT
function formatearRut(rut) {
    rut = rut.replace(/\./g, "").replace(/-/g, "");  // Elimina puntos y guiones
    const numero = rut.slice(0, -1);  // Obtén todos los dígitos excepto el dígito verificador
    const verificador = rut.slice(-1).toUpperCase();  // Obtén el dígito verificador en mayúsculas

    // Formatea el RUT con puntos y guiones
    let rutFormateado = "";
    for (let i = numero.length - 1, j = 0; i >= 0; i--, j++) {
        rutFormateado = numero[i] + rutFormateado;
        if (j === 2 && i !== 0) {
            rutFormateado = "." + rutFormateado;  // Agrega un punto cada 3 dígitos
            j = -1;
        }
    }

    rutFormateado = rutFormateado + "-" + verificador;

    return rutFormateado;
}

// Función para actualizar el valor del campo "rut" en tiempo real
function actualizarRutFormateado() {
    const rutInput = document.getElementById("rut-input");
    const rutValor = rutInput.value;
    const rutFormateado = formatearRut(rutValor);
    rutInput.value = rutFormateado;
}

// Escucha el evento "input" en el campo "rut" y actualiza el valor formateado en tiempo real
document.getElementById("rut-input").addEventListener("input", actualizarRutFormateado);
