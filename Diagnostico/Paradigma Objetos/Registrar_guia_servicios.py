import csv
import re

class Guia:
    def __init__(self,nombre,password,dni,cuit,domicilio,telefono):
        self.nombre = nombre
        self.password = password
        self.dni = dni
        self.cuit = cuit
        self.domicilio = domicilio
        self.telefono = telefono
        
    def validar_cuit(self,cuit):
        #se verifica que los primeros dos dígitos sean 20, 23 o 27, que son los rangos habilitados para guías turísticos
        prefijo = int(self.cuit[:2])
        return prefijo in [20, 23, 27]

class Servicio:
    def __init__(self,titulo, descripcion, ubicacion, precio, fecha_inicio, hora_inicio, tipo_servicio):
        self.titulo = titulo
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.precio = precio
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.tipo_servicio = tipo_servicio

class Sistema_gestor(Guia,Servicio):
    def __init__(self):
        self.guia = []
        self.servicios = []

    def registrar_nuevo_guia(self):
        registro_si_o_no = input ("Registrarse/Iniciar sesion (R/I): ").lower()
        while not (registro_si_o_no == 'r' or registro_si_o_no == 'i'):
            registro_si_o_no = input("Error,Registrarse/Iniciar sesion (R/I):")
        if (registro_si_o_no == 'r'):
            print("REGISTRO DE GUIA")
            print("-" * 40) 
            print("Ingrese los datos personales")
            self.solicitar_datos_personales()
            #Creamos una lista con los valores de cada campo
            self.guia = [self.nombre,self.password,self.dni,self.cuit,self.domicilio,self.telefono]
            print("\nDATOS DEL GUIA")
            print("-" * 40)
            print(f"Nombre: {self.nombre}\nContraseña: {self.password}\nDni: {self.cuit}\nCuit: {self.cuit}\nDomicilio: {self.domicilio}\nTelefono:{self.telefono}")
            confirmacion = input("¿Desea registrar al nuevo guía con estos datos? (S/N): ").lower()
            while not(confirmacion == 's' or confirmacion == 'n'):
                confirmacion = input("Error, letra incorrecta ¿Desea registrar al nuevo guía con estos datos? (S/N): ").lower()
            if confirmacion == "s":
                #Abrimos el archivo CSV en modo append y agregamos una nueva fila con los datos de la guia
                with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\Paradigma Objetos\\guias.csv',mode='a',newline='') as archivo:
                    agregar = csv.writer(archivo, delimiter=',')
                    agregar.writerow(self.guia)
                print("El nuevo guía ha sido registrado con éxito.")
                self.registrar_servicio(self.nombre)
            else:
                print("La operación ha sido cancelada.")
        else:
            self.iniciar_sesion()
    
    def solicitar_datos_personales(self):
        self.nombre = input("Nombre completo: ")
        while not (4 <= len(self.nombre) <= 20):
            self.nombre = input("El nombre debe tener entre 4 y 12 caracteres, por favor ingréselo nuevamente: ")
        self.password = input("Ingrese una contraseña: ")
        while not (len(self.password)>=6):
            self.password= input("La contraseña debe tener mas de 6 caracteres: ")
        self.dni = input("Número de DNI (sin puntos ni guiones): ")
        while not (len(self.dni) == 8 and self.dni.isnumeric()):
            self.dni = input("El DNI debe tener 8 números, por favor ingréselo nuevamente: ")
        self.cuit = input("Número de CUIT (sin guiones): ")
        while not (re.match(r"^\d{11}$", self.cuit) and self.validar_cuit(self.cuit)):
            self.cuit = input("El CUIT ingresado no es válido o no está habilitado, por favor ingréselo nuevamente (sin guiones): ")
        self.domicilio = input("Domicilio: ")
        self.telefono = input("Número de teléfono (sin paréntesis ni guiones): ")
        while not(len(self.telefono) == 8 and self.telefono.isnumeric()):
            self.telefono = input("El telefono ingresado es incorrecto, ingreselo nuevamente (15 mas los 6 numeros)")

    def registrar_servicio(self,nombre_usuario):
        # Solicitar información del servicio
        registrar_nuevo_servicio = input("Desea registrar un nuevo servicio? (S/N): ").lower()
        while not (registrar_nuevo_servicio == 's' or registrar_nuevo_servicio == 'n'):
            registrar_nuevo_servicio = input("Error letra incorrecta, Desea registrar un nuevo servicio? (S/N): ").lower()
        if (registrar_nuevo_servicio == 's'):   
            print("REGISTRO DE SERVICIO")
            print("-" * 40)
            self.titulo = input("Título del servicio: ")
            self.descripcion = input("Descripción del servicio: ")
            self.ubicacion = input("Coordenadas de la ubicación donde se ofrece el servicio (latitud, longitud): ")
            self.precio = float(input("Precio del servicio por persona: "))
            self.fecha_inicio = input("Fecha de inicio del servicio (en formato AAAA/MM/DD): ")
            self.hora_inicio = input("Hora de inicio del servicio (en formato HH:MM): ")
            self.tipo_servicio = input("Tipo de servicio ofrecido: ")
            self.servicios = [self.nombre,self.titulo,self.descripcion,self.ubicacion,self.precio,self.fecha_inicio,self.hora_inicio,self.tipo_servicio]
            print("\nDATOS DEL SERVICIO")
            print("-" * 40)
            print(f"Titulo: {self.titulo}\nDescripcion: {self.descripcion}\nUbicacion: {self.ubicacion}\nPrecio: {self.precio}\nFecha de inicio: {self.fecha_inicio}\nHora de inicio: {self.hora_inicio}\nTipo de servicio: {self.tipo_servicio}")
            confirmacion = input("¿Desea registrar el servicio con estos datos? (S/N): ").lower()
            while not (confirmacion == 's' or confirmacion == 'n'):
                confirmacion = input("Error letra incorrecta, ¿Desea registrar el servicio con estos datos? (S/N): ").lower()
            if confirmacion == 's':
                with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\servicios.csv', mode='a', newline='') as servicios:
                    agregar = csv.writer(servicios,delimiter=',')
                    agregar.writerow(self.servicios)
                print("El servicio ha sido registrado con éxito")
            else:
                print("La operación ah sido cancelada")
        else:
            print("La operación ah sido cancelada")

    def verificar_registro(self,nombre_usuario,password):
        with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\Paradigma Objetos\\guias.csv', mode='r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for fila in reader:
                if len(fila) > 0 and self.nombre == fila[0] and self.password == fila[1]:
                    return True
        return False

    def iniciar_sesion(self):
        print("INICIO DE SESION")
        print("-" * 40)
        self.nombre = input("Nombre de usuario: ")
        self.password = input("Contraseña: ")
        #Verificar si el usuario está registrado
        if self.verificar_registro(self.nombre,self.password):
            print("¡Bienvenido, {}!".format(self.nombre))
            self.registrar_servicio(self.nombre)
        else:
            print("No estás registrado en el sistema!")
            registro = input("Desea registrarse: (S/N)").lower()
            if (registro == 's'):
                self.registrar_nuevo_guia()
            else:
                print("!Hasta luego!")

sistema = Sistema_gestor()
guia= sistema.registrar_nuevo_guia()