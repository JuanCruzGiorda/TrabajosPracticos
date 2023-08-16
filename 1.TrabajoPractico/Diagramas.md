# PROCESO DE NEGOCIO 

![1-trabajopractico](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/e8a69386-e656-49a3-ac2f-a87841b8f129)

# DIAGRAMAS DE SECUENCIA

# Loguear Usuario 

title LOGUEAR USUARIO

PersonaUsuario->IU:Ingresar datos

IU-->Controller:ValidarDatos(datos)

IU<--Controller: Datos validados

PersonaUsuario-->IU: Iniciar Sesion

