# PROCESO DE NEGOCIO 

![1-trabajopractico](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/e8a69386-e656-49a3-ac2f-a87841b8f129)

# DIAGRAMAS DE SECUENCIA

# Loguear Usuario 

title LOGUEAR USUARIO

PersonaUsuario->IU:Ingresar datos

IU-->Controller:ValidarDatos(datos)

IU<--Controller: Datos validados

PersonaUsuario-->IU: Iniciar Sesion

# Registrar Control

title REGISTRAR CONTROL

PersonaUsuario->IU:Seleccionar Punto de Control

IU-->Controller:CargarPuntoControl(idPunto)

IU<--Controller:Información de Punto de Control

PersonaUsuario-->IU: Ingresar datos del producto a controlar

IU-->Controller: CargarProducto(idProducto)

PersonaUsuario->IU:Registrar Resultado (Ok/NoOk)

PersonaUsuario->IU:Cargar Medición (si aplica)

IU-->Controller:RegistrarResultado(idPunto, resultado, medición)

IU<--Controller:Resultado Registrado

