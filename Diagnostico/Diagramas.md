# Diagramas BPMN

Registro de cliente y guia

![0-diagnostico (1)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/5b9b090c-cd76-44c4-87d5-e81a742352d7)

Venta de servicio

![0-1-diagn-stico](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/764429ca-1f83-4a30-bfa6-7b7dee32a868)

# Diagrama de clase - Registro de servicios

![Main](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/50671a48-bd58-4e1e-909b-4a8669cda5b9)

# Diagramas de Secuencia

# Registrar Guia

title REGISTRAR GUIA

PersonaGuia->IU:Ingresar datos personales (nombre, dni, cuit, etc)

IU-->Controller:ValidarDatos(datos personales)

Controller -->ValidadorAfip: BuscarCuit(Cuit)

Controller<--ValidadorAfip: Contribuyente

Controller<--Controller: Comparar datos

Controller-->Persistencia: Guardar Guia

Controller-->Guia: New

IU<--Controller: Pedir Contraseña

PersonaGuia-->IU: Ingresar contraseña

IU-->Controller: Contraseña

# Registrar Servicios

title REGISTRAR SERVICIOS

Guia-->IU: Ingresar email y contraseña

IU-->Controller: Validar_datos(email,contraseña)

Controller-->Persistencia: Validar_datos(email,contraseña)

Controller<--Persistencia: Ingreso correcto(o no)

IU<--Controller: Sesion iniciada

Guia-->IU: Ingresar información del servicio (titulo, descripción, coordenadas, precio por persona, fecha y hora de inicio, tipo de servicio)

IU-->Controller: Verificar_información(titulo, descripción, coordenadas, precio por persona, fecha y hora de inicio, tipo de servicio)

IU<--Controller: Servicio creado con éxito

Controller-->Persistencia: Guardar servicio

Controller-->Servicio: New

# Registrar Cliente

title REGISTRAR CLIENTE

PersonaCliente->IU:Ingresar datos personales (nombre, apellido, DNI, CUIT, domicilio, teléfono, email, ciudad, país de residencia)

IU-->Controller:ValidarDatos(datos personales)

IU<--Controller: Confirmar registro (o no)

PersonaCliente-->IU: Aceptar registro (si o no)

IU-->Controller: Validar confirmacion(si o no)

Controller-->Persistencia: Guardar cliente

Controller-->Cliente: New

# Registrar reserva

title REGISTRAR RESERVA

PersonaCliente->IU:Ingresar fecha

IU-->Controller: ServiciosDisponibles(fecha)

Controller-->Persistencia: ServiciosDisponibles(fecha)

Controller<--Persistencia: Servicios disponibles

IU<--Controller: Mostrar servicios disponibles

PersonaCliente-->IU: Ingresar numero de servicio a contratar

IU-->Controller: ValidarNumeroServicio(numero)

Controller-->Persistencia: ValidarNumeroServicio(numero)

IU<--Controller: Mostrar servicio contratado

PersonaCliente-->IU:Confirmar reserva(si o no)

IU-->Controller:Validar confirmacion(si o no)

IU<--Controller: Pagar

PersonaCliente-->IU: Ingresar tarjeta de credito

IU-->Controller: Validar_tarjeta(datos de tarjeta)

Controller-->Gateway:Validar_tarjeta(datos de tarjeta)

Controller<--Gateway: Pago exitoso(o no)

IU<--Controller: Pago exitoso(o no)

Controller-->Persistencia: Guardar reserva

Controller-->Reserva: New
