function listadoSolicitudes(){
    $.ajax({
        url: "/solicitud/listar_solicitud/",
        type: "get",
        dataType: "json",
        success: function(response){
            if($.fn.DataTable.isDataTable('#bootstrap-data-table')){
                $('#bootstrap-data-table').DataTable().destroy();
            }
            $('#bootstrap-data-table tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]["fields"]['cliente'] + '</td>';
                fila += '<td>' + response[i]["fields"]['banco'] + '</td>';
                fila += '<td>' + response[i]["fields"]['monto_solicitado'] + '</td>';
                fila += '<td>' + response[i]["fields"]['fecha_solicitud'] + '</td>';
                fila += '<td>' + response[i]["fields"]['estado_solicitud'] + '</td>';
                if (response[i]["fields"]['fecha_aprobacion'] === 'Null') {
                    fila += '<td>No Aprobado</td>';
                } else {
                    fila += '<td>' + response[i]["fields"]['fecha_aprobacion'] + '</td>';
                }
                fila += '<td>' + response[i]["fields"]['tipo_credito'] + '</td>';
                fila += '<td> <button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += 'onclick = "abrir_modal_edicion(\'/solicitud/editar_solicitud/'+response[i]['pk']+'/\')"><i class="fa fa-pencil"> Editar</i></button>';
                fila += '<button type = "button" class = "btn btn-danger btn-sm tableButton"';
                fila += 'onclick = "abrir_modal_eliminacion(\'/solicitud/eliminar_solicitud/'+response[i]['pk']+'/\')"><i class="fa fa-trash"> Eliminar</i></button> </td>'
                fila += '</tr>';
                $('#bootstrap-data-table tbody').append(fila);
            }
            $('#bootstrap-data-table').DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de _MAX_ total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                      first: "Primero",
                      last: "Ultimo",
                      next: "Siguiente",
                      previous: "Anterior",
                    },
                },
            }); 
        },
        error: function(error){
            console.log(error);
        }
    });
}

function registrar(){
	activarBoton();
	$.ajax({
		data: $('#form_creacion').serialize(),
		url: $('#form_creacion').attr('action'),
		type: $('#form_creacion').attr('method'),
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoSolicitudes();
			cerrar_modal_creacion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
			mostrarErroresCreacion(error);
            activarBoton()
		}
	})
}

function editar(){
    activarBoton();
    $.ajax({
		data: $('#form_edicion').serialize(),
		url: $('#form_edicion').attr('action'),
		type: $('#form_edicion').attr('method'),
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoSolicitudes();
			cerrar_modal_edicion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
			mostrarErroresEdicion(error);
            activarBoton()
		}
	})
}

function eliminar(pk){
    $.ajax({
        data: {
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
        },
		url: '/solicitud/eliminar_solicitud/'+pk+'/',
		type: 'post',
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoSolicitudes();
			cerrar_modal_eliminacion();
		},
		error: function(error){
            notificacionError(error.responseJSON.mensaje);
		}
	})
}

$(document).ready(function (){
    listadoSolicitudes();
    $("#datepicker").datepicker();
});