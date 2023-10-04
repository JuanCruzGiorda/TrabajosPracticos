# Requerimientos

# Funcionales

Registro de Usuarios:
    
	-Permitir la creacion de usuarios con roles especificos (controladores, supervisores, administradores, etc)

Gestión de información:

	-Proporcionar una interfaz de búsqueda y filtrado eficiente para encontrar información específica sobre maquinas y controles
		   
	-Permitir la vinculacion de información común a multiples planillas, evitando la duplicación de información

Regitro de controles:

	-Permitir registrar los productos a controlar
	   
	-Incluir en el producto las características a controlar y las medidas que este debería tener normalmente
	   
	-Permitir obtener un registro de controles realizados por cada producto, obteniendo datos como el responsable del control, fecha y hora del control.
	   
	-Se debe poder registrar los resultados de controles, tanto los visuales como los de medición

Registro de correciones:

	-Registrar las correcciones realizadas en caso de resultados NoOk
		
	-Mantener un historial de correciones realizadas

Gestión de incidencias:

	-Permitir el registro detallado de incidencias cuando un problema no se puede resolver en el puesto de control
	  
	-Vincular las incidencias con los resultados de control y las acciones tomadas para su resolución

Generación de reportes:

	-Generar informes de control con detalles sobre resultados, correciones, y demás acciones
	   
	-Proporcionar la capacidad de poder exportar informes en diferentes formatos

# No Funcionales

Seguridad:

	-Implementar autentificación y autotrización segura para garantizar que solo usuarios autorizados puedan acceder y realizar cambios
	   
	-Garantizar la protección de los datos importantes almacenados en el sistema

Rendimiento:

	-Permitir manejas múltiples usuarios concurrentes sin pérdida de rendimiento
	   
	-Las búsquedas y filtrados de información deber ser rápidos y eficientes
