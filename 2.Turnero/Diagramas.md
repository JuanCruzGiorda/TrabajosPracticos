# PROTOTIPO

PANTALLA

![Turnero - Diseño de Sistemas](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/26df90bf-925f-480b-bbd2-56716b9ff257)

BOX

![Turnero - Diseño de Sistemas (1)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/8d1bb8a5-829d-4de2-b8ee-59199704cc74)

TÓTEM DE INGRESO (Tablet)

Paso 1

![Turnero - Diseño de Sistemas (2)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/62e28a51-a323-4e58-a8bc-7e41ec5e7ec9)

Paso 2

![Turnero - Diseño de Sistemas (3)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/967df7f0-1410-41b6-8387-480ee0301612)

Paso 3

![Turnero - Diseño de Sistemas (4)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/82a73761-86e2-4f05-9475-d553eef94294)

Paso 4

![Turnero - Diseño de Sistemas (5)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/cecce823-f5be-4d92-a063-6eebb03e4800)

# ARQUITECTURA

Pensamos nuestro sistema como una arquitectura Cliente - Servidor, donde se accede a la app a través de un navegador, y en el cuál el código de la interfaz se encuentra separado del backend. Todo el sistema se instala en un servidor interno de la clínica, y sólo se puede acceder al sistema desde una red local.

![Turnero - Diseño de Sistemas (6)](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/8cdf77b0-6524-4fe3-8b14-2592bff0b537)

BACKEND

El backend, que se puede implementar con tecnologías como Node o Java, está a su vez dividido en capas:

1. Infraestructura: Esta sección se encarga del procesamiento primario de las requests HTTP, validación de parámetros, parseo de los datos recibidos, y serialización de los datos a entregar.

2. Dominio: Aquí se encuentran las reglas de dominio de nuestro sistema, las clases denominadas Services se encargan de ejecutar los casos de uso de la aplicación.

3. Persistencia / Base de Datos: Esta capa tiene la responsabilidad de comunicar al sistema con la base de datos, y provee una interfaz reutilizable y concreta a la capa de dominio.

Cabe aclarar que el orden de comunicación entre estas capas es Infraestructura -> Dominio -> Persistencia.

FRONTED

Nuestro sistema ofrece tres experiencias de usuario muy diversas, la de la pantalla de la sala de espera, la del turnero que ve el paciente al ingresar, y la vista del box, que utiliza la secretaria. 
Entre otras diferencias, la pantalla y el turnero no necesitan autenticación, mientras que el box sí. Por ello pensamos en utilizar tres aplicaciones frontend separadas, cada una con su propia lógica, pero conectadas al mismo servidor backend. Todas ellas pueden ser implementadas como SPAs (Single Page Applications) usando herramientas como React o Vue.

Descripción de cada frontend:

1. Pantalla: En ella se muestra el listado de turnos ya atendidos, y los próximos a ser atendidos. Para actualizar dicho listado se utiliza la técnica de Polling, donde se realizan peticiones al backend cada 15 segundos.

2. Turnero (paciente): Se trata de una vista responsiva, descrita en el prototipo, que no requiere autenticación.

3. Secretaria (box): La parte quizás más compleja del frontend, ya que además de la vista donde se presentan los turnos y sus estados, también se agrega la funcionalidad de login.

# PROCESO DE NEGOCIO

![2-turnero](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/560ef858-74d4-4284-add7-2e9aa777c2b6)

# Diagrama de Clase

![Main](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/7603e929-e27f-4225-ba42-6c3aeff0c4c2)

# DIAGRAMAS DE SECUENCIA

# Registrar paciente

title Registrar Paciente

PersonaPaciente->IU: Ingresar datos personales(nombre, dni, obra social, telefono)

IU-->Controller: Datos personales

Controller-->Controller: Validar_datos(datos personales)

IU<--Controller: Confirmacion de registro(o no)

Controller-->Persistencia: Registrar nuevo paciente

Persistencia-->Paciente: New

# Registrar turno

title Registrar Turno

Paciente->IU: Ingresar dni

IU-->Controller: dni

Controller-->Persistencia: Validar_identidad(dni)

Controller<--Persistencia: Confirmar identidad(o no)

IU<--Controller: Pedir datos del turno 

Paciente-->IU: Ingresar datos (doctor, fecha)

IU-->Controller: doctor, fecha

Controller-->Persistencia: Validar_datos(datos)

Controller<--Persistencia: Datos validados(o no)

IU<--Controller: Confirmacion de turno

Paciente-->IU: Confirmar turno

IU-->Controller: Confirmación

Controller-->Controller: Verificar_Confirmacion()

Controller-->Persistencia: Registrar turno

Persistencia-->Turno: New

# Búsqueda de turno (con turno previo)

title Proceso Turnero (turno previo)

Paciente-->IU: Seleccionar opción con turno

IU-->Controller: Solicitar ingreso de Dni

IU<--Controller: Mostrar campo para ingresar Dni

Paciente-->IU: Ingresar Dni

IU-->Controller: Verificar_existencia_turno(Dni)

Controller-->Persistencia: Verificar_existencia_turno(Dni)

Controller<--Persistencia: Lista de turnos existentes

IU<--Controller: Mostrar lista de turnos

Paciente-->IU: Seleccionar turno

IU-->Controller: Enviar turno seleccionado

Controller-->Persistencia: Confirmar turno

Controller<--Persistencia: Codigo de fila

IU<--Controller: Mostrar codigo de fila

# Búsqueda de turno (sin turno previo)

title Proceso Turnero (sin turno previo)

Paciente-->IU: Seleccionar opción sin turno

IU-->Controller: Solicitud de generación de código

Controller<--Controller: Generar código

Controller-->Persistencia: Guardar código

IU<--Controller: Mostrar código

# MAPEO DE OBJETOS A TABLAS
![drawSQL-turnero-export-2023-10-10](https://github.com/JuanCruzGiorda/TrabajosPracticos/assets/114437428/ae3347b7-07da-44b1-9bb8-eb1a7481e5f0)
