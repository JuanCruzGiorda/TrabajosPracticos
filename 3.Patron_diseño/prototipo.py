import copy

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class ListaDePrecios:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def clonar(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    lista_base = ListaDePrecios()
    lista_base.agregar_producto(Producto("Producto 1", 100))
    lista_base.agregar_producto(Producto("Producto 2", 200))
    lista_base.agregar_producto(Producto("Producto 3", 300))

    lista_derivada = lista_base.clonar()

    for producto in lista_derivada.productos:
        producto.precio *= 0.9

    print("Lista Base:")
    for producto in lista_base.productos:
        print(producto)

    print("\nLista con Descuento:")
    for producto in lista_derivada.productos:
        print(producto)
