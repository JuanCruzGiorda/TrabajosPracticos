# Diagrama BPMN

![diagnostico](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/cbd90e29-224b-4a8d-ab9d-07ff97eccca1)

# Diagramas de Secuencia

Registrar Guia

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

Registrar Usuario

title REGISTRAR USUARIO

PersonaUsuario->IU:Ingresar datos
IU-->Controller:ValidarDatos(datos)
IU<--Controller: Confirmar registro
PersonaUsuario-->IU: Aceptar registro
IU-->Controller: Validar confirmacion
Controller-->Usuario: New
PersonaUsuario-->IU: Iniciar Sesion
PersonaUsuario-->IU: Ingresar usuario y contraseña
IU-->Controller: ValidarDatos(datos)
IU<--Controller: Inicio Correcto

