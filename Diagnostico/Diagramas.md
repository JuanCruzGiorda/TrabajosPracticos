# Diagrama BPMN

![diagnostico (1)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/982aefa7-de5a-4f7b-887c-4e7fb05b1a07)

# Diagramas de Secuencia

# Registrar Guia

title REGISTRAR GUIA	

PersonaGuia->IU:Ingresar datos

IU-->Controller:ValidadDatos(datos)

Controller -->ValidadorAfip: BuscarCuit(Cuit)

ValidadorAfip -->Contribuyente: New

Controller<--ValidadorAfip: Contribuyente

Controller<--Controller: Comparar datos

Controller-->Guia: New

IU<--Controller: Pedir Contraseña

IU-->Controller: Contraseña

Controller-->Persistencia: Guardar Guia

# Registrar Cliente

title REGISTRAR CLIENTE

PersonaCliente->IU:Ingresar datos

IU-->Controller:ValidarDatos(datos)

IU<--Controller: Confirmar registro

PersonaCliente-->IU: Aceptar registro

IU-->Controller: Validar confirmacion

Controller-->Cliente: New

PersonaCliente-->IU: Iniciar Sesion

PersonaCliente-->IU: Ingresar usuario y contraseña

IU-->Controller: ValidarDatos(datos)

IU<--Controller: Inicio Correcto

# Registrar reserva

title REGISTRAR RESERVA

PersonaCliente->IU:Ingresar fecha

IU-->Controller: ServiciosDisponibles(fecha)

IU<--Controller: Mostrar servicios disponibles

PersonaCliente-->IU: Ingresar numero de servicio a contratar

IU-->Controller: ValidarNumeroServicio(numero)

IU<--Controller: Mostrar servicio contratado

PersonaCliente-->IU:Confirmar reserva

IU-->Controller:Validar confirmacion

Controller-->Reserva: New


