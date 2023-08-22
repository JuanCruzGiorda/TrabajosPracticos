# PROCESO DE NEGOCIO 

![1-trabajopractico](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/e8a69386-e656-49a3-ac2f-a87841b8f129)

# DIAGRAMAS DE SECUENCIA

# Loguear Usuario 

title LOGUEAR USUARIO

PersonaUsuario->IU: Ingresar usuario y contraseña 

IU-->Controller: Validar_datos(datos)

Controller-->Persistencia: Validar_datos(datos)

Controller<--Persistencia: Datos correctos(o no)

IU<--Controller: Ingreso correcto

PersonaUsuario-->IU: Iniciar Sesion

# Registrar Control

title REGISTRAR CONTROL

Usuario->IU: Seleccionar Punto de Control

IU-->Controller: CargarPuntoControl(idPunto)

Controller-->Persistencia: CargarPuntoControl(idPunto)

Controller<--Persistencia: Punto de control correcto(o no)

IU<--Controller:Información del Punto de Control

Usuario-->IU: Ingresar datos del producto a controlar

IU-->Controller: CargarProducto(datos)

Usuario-->IU:Registrar Resultado (Ok/NoOk)

Usuario-->IU:Cargar Medición (si aplica)

IU-->Controller:RegistrarResultado(idPunto, resultado, medición)

Controller-->Control: New

Controller-->Persistencia: Guardar resultado

IU<--Controller: Resultado Registrado

