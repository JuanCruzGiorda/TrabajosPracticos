# Requerimientos

# Funcionales

Registro de Guías Turísticos:

    -Los guías deben poder registrarse proporcionando sus datos personales (nombre, apellido, dni, cuit, domicilio, telefono, email, ciudad, pais de residencia).

Creación de Tipos de Servicios:

    -Los guías deben tener la opción de dar de alta nuevos tipos de servicios turísticos.

Registro de Ofertas de Servicios Turísticos:

    -Los guías turísticos deben poder registrar nuevas ofertas de servicios.

    -Se debe poder ingresar diferentes tipos de información (titulo, descripcion, ubicacion en coordenadas, precio por persona, fecha y hora de inicio, tipo de servicio ofrecido.

Consulta de Oferta de Servicios Turísticos:

    -Los usuarios deben poder buscar y consultar la oferta de servicios turísticos por tipo y ubicación.

Registro de Cliente:

    -Los clientes deben poder registrarse proporcionando sus datos personales (nombre, apellido, DNI, CUIT, domicilio, teléfono, email, ciudad, país de residencia).

Reserva de Servicios Turísticos:

    -Los clientes registrados deben poder reservar servicios turísticos.
  
    -Se debe poder seleccionar los servicios deseados, fecha y cantidad de personas (por cada persona que integra el grupo se debe ingresar nombre, apellido y DNI).
  
    -Debe haber opción para pagar la reserva con tarjeta de crédito.
  
    -Debe generarse un voucher provisorio que se envía por email, si el pago es exitoso.

Pago de Saldo y Emisión de Vouchers Definitivos:

    -Los clientes deben poder abonar el saldo restante en varios pagos.
  
    -El sistema debe enviar el voucher definitivo por email al cliente una vez que el saldo esté totalmente pago.

Generación de Listado de Insumos:

    -Desde el área de logística se debe poder generar un listado de insumos necesarios para los servicios contratados próximos a realizarse.
  
    -El listado debe agrupar por tipo de servicio y cantidad de personas.

Gestión de Órdenes de Compra:

    -El personal de logística debe poder generar órdenes de compra para los insumos necesarios.
  
    -Debe haber un proceso de control de recepción de la compra por parte del proveedor.
  
    -Se debe poder generar un reclamo al proveedor en caso de algun problema.

Gestión de Reservas y Estado de Servicios:

    -La persona a cargo debe poder controlar la cantidad de personas en el servicio.
  
    -Se debe permitir acreditar la identidad de las personas presentes.
  
    -Si alguien no puede asistir, se debe permitir indicarlo en la reserva.

    -La reserva debe pasar al estado "en curso" cuando el servicio comienza y al estado "realizada" al finalizar.

Registro de Problemas y Feedback:

    -La persona a cargo debe poder registrar problemas o feedback después de que el servicio termine.
  
    -Debe proporcionarse una forma de registrar la fecha y hora de finalización.

# Requerimientos no funcionales

Seguridad:

    -El sistema debe garantizar la privacidad de los datos personales y de pago de los clientes.
  
    -La información de las transacciones de tarjeta de crédito debe ser segura y cumplir con estándares de seguridad.

Usabilidad:

    -La interfaz de usuario debe ser intuitiva y fácil de usar tanto para guías como para clientes.
  
    -Los procesos de registro, reserva y pago deben ser simples.

Integración con Web Services Externos:

    -Debe haber una integración eficiente con el Web Service de AFIP para la validación del CUIT de los guías.
