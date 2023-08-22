# Diagrama BPMN

![diagnostico (1)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/982aefa7-de5a-4f7b-887c-4e7fb05b1a07)

# Diagramas de Secuencia

# Registrar Guia

title REGISTRAR GUIA

PersonaGuia->IU:Ingresar datos

IU-->Controller:ValidarDatos(datos)

Controller -->ValidadorAfip: BuscarCuit(Cuit)

Controller<--ValidadorAfip: Contribuyente

Controller<--Controller: Comparar datos

Controller-->Guia: New

IU<--Controller: Pedir Contraseña

PersonaGuia-->IU: Ingresar contraseña

IU-->Controller: Contraseña

Controller-->Persistencia: Guardar Guia

# Registrar Servicios

title REGISTRAR SERVICIOS

Guia-->IU: Ingresar mail y contraseña

IU-->Controller: Validar_datos(datos)

Controller-->Persistencia: Validar_datos(datos)

Controller<--Persistencia: Ingreso correcto(o no)

IU<--Controller: Sesion iniciada

Guia-->IU: Ingresar información del servicio

IU-->Controller: Verificar_información()

IU<--Controller: Servicio creado con éxito

Controller-->Servicio: New

Controller-->Persistencia: Guardar servicio

# Registrar Cliente

title REGISTRAR CLIENTE

PersonaCliente->IU:Ingresar datos

IU-->Controller:ValidarDatos(datos)

IU<--Controller: Confirmar registro (o no)

PersonaCliente-->IU: Aceptar registro

IU-->Controller: Validar confirmacion()

Controller-->Cliente: New

Controller-->Persistencia: Guardar cliente

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

PersonaCliente-->IU:Confirmar reserva

IU-->Controller:Validar confirmacion

Controller-->Reserva: New

Controller-->Persistencia: Guardar reserva
