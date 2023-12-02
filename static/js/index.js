function eliminar(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
        },
		url: '/pago/eliminar_pago/'+pk+'/',
		type: 'post',
		success: function(response){
            notificacionSuccess(response.mensaje);
			cerrar_modal_eliminacion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
		}
	})
}

function aprobarPago(pagoId) {
	// Obtén el token CSRF
	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

	$.ajax({
		url: `/pago/aprobar_pago/${pagoId}/`,
		type: 'POST',
		dataType: 'json',
		// Incluye el token CSRF en la solicitud
		headers: { "X-CSRFToken": csrfToken },
		success: function (data) {
			console.log(data);
			// Aquí puedes manejar la respuesta, actualizar la interfaz de usuario, etc.
			// Por ejemplo, puedes recargar la lista de pendientes.
			cargarPagosPendientes();  // Asegúrate de tener una función para cargar pagos pendientes.
		},
		error: function (error) {
			console.log(error);
		}
	});
}