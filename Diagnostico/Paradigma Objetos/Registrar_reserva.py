import csv
import re

class Usuario:
    def __init__(self,nombre,password,dni,cuit,email,telefono):
        self.nombre_usuario = nombre
        self.password = password
        self.dni = dni
        self.cuit = cuit
        self.email = email
        self.telefono = telefono
    
class Reserva:
    def __init__(self,fecha,estado): 
        self.fecha_servicio = fecha
        self.estado = estado

class Sistema_gestor(Usuario,Reserva):
    def __init__(self):
        self.usuario = []

    def registrar_usuario(self):
        registrar_nuevo_usuario = input ("Registrarse/Iniciar sesion (R/I): ").lower()
        while not (registrar_nuevo_usuario == 'r' or registrar_nuevo_usuario == 'i'):
            registrar_nuevo_usuario = input ("Error letra incorrecta, Registrarse/Iniciar sesion (R/I): ").lower()
        if (registrar_nuevo_usuario == 'r'):
            print("\nREGISTRO DE USUARIO")
            print("-" * 40) 
            print("Ingrese los datos personales")
            self.solicitar_datos_personales()
            self.usuario = [self.nombre_usuario,self.password,self.dni,self.cuit,self.email,self.telefono]
            print("\nDATOS DEL USUARIO")
            print("-" * 40)
            print (f"Nombre: {self.nombre_usuario}\nContraseña: {self.password}\nDni: {self.dni}\nCuit: {self.cuit}\nEmail: {self.email}\nTelefono: {self.telefono}")
            print("-" * 40)
            confirmacion_usuario = input("¿Desea registrarse con estos datos? (S/N): ").lower()
            while not (confirmacion_usuario == 's' or confirmacion_usuario == 'n'):
                confirmacion_usuario = input("Error letra incorrecta, ¿Desea registrarse con estos datos? (S/N): ").lower()
            if confirmacion_usuario  == "s":
                #Abrimos el archivo CSV en modo append y agregamos una nueva fila con los datos del usuario
                with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\usuarios.csv',mode='a',newline='') as archivo:
                    agregar = csv.writer(archivo, delimiter=',')
                    agregar.writerow(self.usuario)
                print("Se ha registrado con éxito")
                self.registrar_reserva(self.nombre_usuario)
            else:
                print("La operación ha sido cancelada.")
        else:
            self.iniciar_sesion()
    
    def solicitar_datos_personales(self):
        self.nombre_usuario = input("Nombre completo: ")
        while not (4 <= len(self.nombre_usuario) <= 20):
            self.nombre_usuario = input("El nombre debe tener entre 4 y 12 caracteres, por favor ingréselo nuevamente: ")
        self.password = input("Ingrese una contraseña: ")
        while not (len(self.password)>=6):
            self.password= input("La contraseña debe tener mas de 6 caracteres: ")
        self.dni = input("Número de DNI (sin puntos ni guiones): ")
        while not (len(self.dni) == 8 and self.dni.isnumeric()):
            self.dni = input("El DNI debe tener 8 números, por favor ingréselo nuevamente: ")
        self.cuit = input("Número de CUIT (sin guiones): ")
        while not (re.match(r"^\d{11}$", self.cuit) and self.validar_cuit(self.cuit)):
            self.cuit = input("El CUIT ingresado no es válido, por favor ingréselo nuevamente (sin guiones): ")
        self.email = input("Email: ")
        self.telefono = input("Número de teléfono (sin paréntesis ni guiones): ")
        while not(len(self.telefono) == 8 and self.telefono.isnumeric()):
            self.telefono = input("El telefono ingresado es incorrecto, ingreselo nuevamente (15 mas los 6 numeros)")

    def iniciar_sesion(self):
        print("INICIO DE SESION")
        print("-" * 40)
        self.nombre_usuario = input("Nombre de usuario: ")
        self.password = input("Contraseña: ")
        #Verificar si el usuario está registrado
        if self.verificar_registro(self.nombre_usuario,self.password):
            print("¡Bienvenido, {}!".format(self.nombre_usuario))
            self.registrar_reserva(self.nombre_usuario)
        else:
            print("Contraseña o Usuario incorrecto")
            registro = input("Desea registrarse: (S/N)").lower()
            while not (registro == 's' or registro == 'n'):
                registro = input("Desea registrarse: (S/N)").lower()
            if (registro == 's'):
                self.registrar_usuario()
            else:
                print("!Hasta luego!")
    
    def verificar_registro(self,nombre_usuario,password):
        with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\usuarios.csv', mode='r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for fila in reader:
                if len(fila) > 0 and self.nombre_usuario == fila[0] and self.password == fila[1]:
                    return True
        return False
    
    def validar_cuit(self,cuit):
        #se verifica que los primeros dos dígitos sean 20, 23, 24 o 27
        prefijo = int(self.cuit[:2])
        return prefijo in [20, 23, 24, 27]
    
    def registrar_reserva(self,nombre_usuario):
        # Mostrar servicios disponibles
        servicios_disponibles = []
        with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\servicios.csv', mode='r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for fila in reader:
                if len(fila) >= 8:
                    servicios_disponibles.append((fila[7],fila[5]))
        print("\nSERVICIOS DISPONIBLES")
        print("-" * 40)
        for i, servicio in enumerate(servicios_disponibles):
            print(f"{i+1}. {servicio}")

        #Ingresar la fecha que quiere realizar alguna actividad
        self.fecha_servicio = input("Ingrese la fecha en que desea realizar el servicio, teniendo en cuenta las disponibles (en formato AAAA/MM/DD): ")

        #Buscar servicios disponibles en la fecha seleccionada
        servicios_disponibles_fecha = []
        with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\servicios.csv', mode='r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for fila in reader:
                if fila[5] == self.fecha_servicio:
                    servicios_disponibles_fecha.append(fila[7])
        if servicios_disponibles_fecha:
            print("\nSERVICIOS DISPONIBLES EN LA FECHA SELECCIONADA")
            print("-" * 40)
            for i, servicio in enumerate(servicios_disponibles_fecha):
                print(f"{i+1}. {servicio}")

            #Ingresar servicios a contratar
            seleccion_servicio = input("Ingrese el número del servicio que desea contratar (o 'q' para terminar): ")
            servicios_contratados = []
            while seleccion_servicio != 'q':
                if not seleccion_servicio.isdigit() or int(seleccion_servicio) < 1 or int(seleccion_servicio) > len(servicios_disponibles_fecha):
                    print("Número de servicio no válido.")
                elif servicios_disponibles_fecha[int(seleccion_servicio)-1] in servicios_contratados:
                    print("Ya ha seleccionado ese servicio.")
                else:
                    servicios_contratados.append(servicios_disponibles_fecha[int(seleccion_servicio)-1])
                    print(f"Servicio {servicios_disponibles_fecha[int(seleccion_servicio)-1]} agregado.")
                seleccion_servicio = input("Ingrese el número del servicio que desea contratar (o 'q' para terminar): ")
        
            # Mostrar servicios contratados
            if servicios_contratados:
                print("\nSERVICIOS CONTRATADOS")
                print("-" * 40)
                for servicio in servicios_contratados:
                    print(servicio)

                #Guardar información de la reserva
                self.estado = "pendiente"
                with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\reservas.csv', mode='a', newline='') as archivo_csv:
                    writer = csv.writer(archivo_csv)
                    for servicio in servicios_contratados:
                        writer.writerow([self.nombre_usuario,servicio,self.fecha_servicio,self.estado])
                print("Reserva guardada con éxito.")
                self.mostrar_reservas(self.nombre_usuario)
            else:
                print("No ha contratado ningún servicio.")
        else:
            print("No hay servicios disponibles en la fecha seleccionada.")
            
    def mostrar_reservas(self,nombre_usuario):
        print("-" * 40)
        print(f"\nRESERVAS EXISTENTES DE {self.nombre_usuario.upper()}")
        print("-" * 40)
        with open('C:\\Users\\Usuario\\Desktop\\UTN\\3-Año\\Diseño de Sistemas\\1-TP\\Paradigma Objetos\\reservas.csv', mode='r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for fila in reader:
                if len(fila) > 0 and self.nombre_usuario == fila[0]:
                        print(f"Servicio: {fila[1]} - Fecha: {self.fecha_servicio} - Estado: {self.estado}")
                        
print("\nSISTEMA DE RESERVAS")
print("-" * 60)
sistema = Sistema_gestor()
reserva = sistema.registrar_usuario()
