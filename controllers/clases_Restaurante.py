from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressDialog
from PySide6.QtGui import QPixmap
import sys, time, pickle
import datetime
from PySide6.QtCore import Qt
import os

class Factura:
    def __init__(self):
        self.numero = None
        self.provedor = None
        self.items = []
        self.total = 0

    def generar_factura(self,numero,proveedor,items,total):#en el caso 
        self.numero = numero
        self.provedor = proveedor
        self.items = items
        self.total = self.total + total
        
        # el siguiente metodo es lo mismo pero da un tratamiento en el caso de que no 
        # se envie un total y se envien una lista de objetos de productos
        
    # def generar_factura(self,numero,proveedor,items):#en el caso 
    #     self.numero = numero
    #     self.provedor = proveedor
    #     self.items = items
    #     self.Total(items)
        
    # def Total(self,item):
    #     for i in item:
    #         self.total = self.total + i.precio
        
        

    

    # def ver_detalle(self):
    #     detalle = f"Factura {self.numero} - Cliente: {self.cliente}\n"
    #     for producto, cantidad, precio_unitario in self.items:
    #         detalle += f"{producto} x{cantidad}: ${precio_unitario * cantidad:.2f}\n"
    #     detalle += f"Total: ${self.total:.2f}"
    #     return detalle
    
    
class Cliente:
    def __init__(self, nombre, contacto,estado,foto):
        self.nombre = nombre
        self.contacto = contacto
        self.estado = estado# nomal o preferencial
        self.foto= foto

    def realizar_orden(self, orden):
        self.historial_ordenes.append(orden)

    def actualizar_contacto(self, nuevo_contacto):
        self.contacto = nuevo_contacto

    def agregar_preferencia(self, estado):
        self.estado = estado

    def ver_historial_ordenes(self):
        return self.historial_ordenes
    
class Programa():
    
    def __init__(self):
        self.lista_empleados = {}
        self.lista_proveedores = {}
        self.lista_tiquetera = {}
        self.bodega = {}
        self.clientes = []
        self.platos = []
        self.dineroCaja = None
        self.nro = 1
        
    # CLIENTES
    
    def agregar_cliente(self,nombre,contacto,estado, foto):
        if self.buscar_cliente != False:            
            cliente = Cliente(nombre,contacto,estado,foto)
            self.clientes.append(cliente)
            print('cliente añadido con exito')
            
    def eliminar_cliente(self,contacto):
        if a := self.buscar_cliente(contacto):
            self.clientes.remove(a)
        
        
    def cambiar_contactoCliente(self,contacto,nuevoContacto):
        for i in self.clientes:
            if i.contacto == contacto:
                i.actualizar_contacto(nuevoContacto)
                break
            
    def buscar_cliente(self, contacto):
        clientes_filtrados = filter(lambda i: i.contacto == contacto, self.clientes)
        return next(clientes_filtrados, False)
    
    def dar_puntosCliente(self,contacto):
        if i := self.buscar_cliente(contacto):
            i.puntos_lealtad += 15
        
        
    # DINERO EN CAJA
    def sumar_dinero(self,dinero):
        if self.dineroCaja != None:
            self.dineroCaja = self.dineroCaja+dinero
        else : self.dineroCaja = dinero
        
    def restar_dinero(self,dinero):
        if self.dineroCaja != None:
            if self.dineroCaja > dinero:
                self.dineroCaja = self.dineroCaja-dinero
            else: return False
        else : return False
    
    
        
    # VENDER
    def vender_platos(self,platos):
        total = 0
        for i in platos:
            total = total+i.precio
            
        self.sumar_dinero(total)
        
    def devolucion_pedido(self,platos):
        total = 0
        for i in platos:
            total = total+i.precio
            
        self.restar_dinero(total)
    
    
    
    # EMPLEADOS
    def añadir_empleado(self,nombre,cedula,cargo,salario):
        if cedula in self.lista_empleados:
            return False
        else:
            self.lista_empleados.update({cedula:{'Nombre':nombre,'CC':cedula,'Cargo':cargo,'Salario':salario}})
        
    def eliminar_empleado(self,cc):
        if cc in self.lista_empleados:
            del self.lista_empleados[cc]
        else: return False
    
    def cambiar_nombreE(self,cc,nombre):
        if cc in self.lista_empleados:
            self.lista_empleados[cc]['Nombre'] = nombre
        else: return False
    
    def cambiar_cedulaE(self,cc,cedulanueva):
        if cc in self.lista_empleados:
            self.lista_empleados[cc]['CC'] = cedulanueva
            valor = self.lista_empleados.pop(cc)
            self.lista_empleados[cedulanueva] = valor
        else: return False
        
    def cambiar_cargoE(self,cc,cargo):
        if cc in self.lista_empleados:
            self.lista_empleados[cc]['Cargo'] = cargo
        else: return False
        
    def cambiar_salarioE(self,cc,salario):
        if cc in self.lista_empleados:
            self.lista_empleados[cc]['Salario'] = salario
        else: return False
        
    def buscar_empleado(self,cc):
        if cc in self.lista_empleados:
            return list(self.lista_empleados[cc].values())
        else: return False
        
    # TIQUETERA     
    
    def añadir_tiquetera(self,cliente,fin,comidas):
        # Asignar el numero de la tiquetera 
        nro = f'000{self.nro+1}'
        if len(nro) > 4:
            nro = nro[1:]
            
        # Asignar la fech de inicio a la tiquetera
        fecha = datetime.datetime.now()   
        inicio = fecha.date()
        inicio = inicio.strftime('%d/%m/%Y')
        
        #crear tiquetera
        self.lista_tiquetera.update({nro:{'Cliente':cliente,'Inicio':inicio,'Fin':fin,'Comidas':comidas, 'Nro':nro}})
        
    def eliminar_tiquete(self,nro):
        if nro in self.lista_tiquetera:
            del self.lista_tiquetera[nro]
        else: return False
        
    def cambiar_finT(self,nro,fin):
        if nro in self.lista_tiquetera:
            self.lista_tiquetera[nro]['Fin'] = fin
        else: return False
        
    def cambiar_ComidasT(self,nro,comidas):
        if nro in self.lista_tiquetera:
            self.lista_tiquetera[nro]['Comidas'] = comidas
        else: return False
        
    def buscar_tiquetera(self,nro):
        if nro in self.lista_tiquetera:
            return    list(self.lista_tiquetera[nro].values())
        else: return False
        
        
    # PROVEEDORES
    def añadir_proveedor(self,nombre,cell,id,productos):
        if nombre in self.lista_proveedores:
            return False
        else:
            self.lista_proveedores.update({id:{'Proveedor':nombre,'Telefono':cell,'ID':id,'Productos':productos}})
        
    def eliminar_provedor(self,id):
        if id in self.lista_proveedores:
            del self.lista_proveedores[id]
        else: return False
        
    def cambiar_nombreP(self,id,nombre):
        if id in self.lista_proveedores:
            self.lista_proveedores[id]['Proveedor'] = nombre
        else: return False
        
    def cambiar_telefonoP(self,id,cell):
        if id in self.lista_proveedores:
            self.lista_proveedores[id]['Telefono'] = cell
        else: return False
    
    def cambiar_IdProveedores(self,id,IDnueva):
        if id in self.lista_proveedores:
            self.lista_proveedores[id]['ID'] = IDnueva
            self.lista_proveedores[IDnueva] = self.lista_proveedores.pop(id)
        else: return False
        
    def eliminar_productoP(self,id,producto):
        if id in self.lista_proveedores:
            if producto in self.lista_proveedores[id]['Producto']:
                self.lista_proveedores[id]['Producto'].remove(producto) # Elimina el producto
        else : return False
        
    def agregar_productoP(self, id, producto):
        if id in self.lista_proveedores:
            if producto not in self.lista_proveedores[id]['Producto']:
                self.lista_proveedores[id]['Producto'].append(producto)
                return True  # Producto agregado con éxito
            else:
                return False  # Producto ya existe en la lista
        else:
            return False
        
    # BODEGA
    
    def añadir_producto(self,nombre,cantidad):
        if nombre in self.bodega == False:
            self.bodega.update({nombre:{'Nombre':nombre,'Cantidad':cantidad}})
        else: return False
    
    def eliminar_productoBodega(self,producto):# pasas el nombre del producto
        if producto in self.bodega:
            del self.bodega[producto]
        else: return False
        
    def buscar_productoBodega(self,nombreproducto):#
        if nombreproducto in self.bodega:
            i  = self.bodega[nombreproducto]
            return list(i.values())
        else: return False
        
    def cambiar_cantidadBodega(self,producto,cantidad):
        self.bodega[producto]['Cantidad'] = cantidad
        
    # PLATOS
    def agregar_plato(self,nombre,precio):
        plato = Platos()
        plato.nombre = nombre
        plato.precio = precio
        self.platos.append(plato)
        
    def eliminar_plato(self,nombre):
        for i in self.platos:
            if nombre == i.nombre:
                self.platos.remove(i)
                break
            
    def cambiar_nombrePlato(self,nombre):
        for i in self.platos:
            if nombre == i.nombre:
                i.nombre = nombre
        
    def cambiar_precioPlato(self,nombre,precio):
        for i in self.platos:
            if nombre == i.nombre:
                i.precio = precio
                
    def mostrar_platos(self):# retorna un diccionario con el nombre y el precio de los platos
        menu = {}
        for i in self.platos:
            menu.update({'Plato':i.nombre,'Precio':i.precio})
            return menu
        
class restaurante():
    def __init__(self):
        self.programa = Programa()
        
    def hacer_pedido(self):
        
        
    
        pass      

 
class Platos():
    def __init__ (self):
        self.nombre = None
        self.precio = None
        
    def setNombrePlato(self,nombre):
        self.nombre = nombre 
     
    def setNombrePlato(self,precio):
        self.precio = precio 
        

    
    
    
# class Proveedores():
    
#     def __init__(self,proveedor,telefono):
#         self.proveedor = proveedor
#         self.telefono = telefono
#         self.prouctos = {}
        
#     def productos(self):
#         self.productoss
        
        
        
        
class Producto():
    def __init__ (self):
        self.nombre = None
        self.precio = None
        self.cantidad = None
        self.distribuidor  = []      
        
        
          
    
# class Empleado():
#     def __init__(self,nombre,cedula,cargo):
#         self.nombre = nombre
#         self.cedula = cedula
#         self.cargo = cargo
#         self.darSalario(cargo)
    
#     def darSalario(self,cargo):
#         match cargo:
#             case 'Mesero':
#                 self.salario = 1_200_000
#             case 'Limpieza':
#                 self.salario = 1_200_000
#             case 'Cosinero':
#                 self.salario = 1_600_000
#             case 'Chef de cosina':
#                 self.salario = 2_000_000
 
 
 
# class Tiquetera():
#     def __init__(self,cliente,fecha_inicio,fecha_final,nro_comidas,nro):
#         self.nombre_cliente = cliente
#         self.fecha_inicio = fecha_inicio
#         self.fecha_final = fecha_final
#         self.nro_comidas = nro_comidas
        

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  
        self.resize(1000,600)



        
def main():
    
    # Cargar datos
    # datos_cargados = cargar_datos()
    # datos_cargados.añadir_empleado(input('Nombre:'),input('CC:'),input('Cargo:'),input('Salario:'))
    # print(datos_cargados.lista_empleados)
    
    program = Programa()
    # program.añadir_empleado('maria',123,'mesera',200000)
    # print(program.buscar_empleado(123))
    # program.cambiar_nombreE(123,'juan pablo')
    # program.cambiar_cargoE(123,'cocinero')
    # program.cambiar_salarioE(123,120000)
    # program.cambiar_cedulaE(123,234)
    # print(program.buscar_empleado(234))
    # print(program.lista_empleados.keys())
    # program.eliminar_empleado(234)
    # print(program.buscar_empleado(123))
    
    # program.añadir_cliente( input('nombre'),h := input('contacto'))
    # program.cambiar_contactoCliente(h,j := 1234)
    # program.dar_puntosCliente(j)
    # print(program.clientes)
    # program.eliminar_cliente(j)
    # print(program.clientes)
    
    program.añadir_tiquetera('Carlos','15/04/2023',30)
    print(program.lista_tiquetera)
    a = list(program.lista_tiquetera.keys())
    print(a)
    a = a[0]
    program.cambiar_ComidasT(a,28)
    print(program.lista_tiquetera)
    program.cambiar_finT(a,'12/09/2023')
    print(program.lista_tiquetera)
    program.eliminar_tiquete(a)
    print(program.lista_tiquetera)
    
    # Guardar datos
    # guardar_datos(datos_cargados)
    # print("Datos guardados.")
            
def guardar_datos(programa):
    with open(archivo, 'wb') as f:
        pickle.dump(programa, f)
        
def cargar_datos():
    try:
        with open(archivo, 'rb') as f:  # Cambio: modo 'rb' para leer binario
            programa = pickle.load(f)
            return programa
    except (FileNotFoundError, pickle.UnpicklingError):
        print(f"El archivo '{archivo}' no existe o no se puede cargar. Se creará uno nuevo.")
        programa_nuevo = Programa()
        guardar_datos(programa_nuevo)  # Crear y guardar un nuevo archivo
        return programa_nuevo
ruta= os.path.join("database", "archivo")
archivo = ruta

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        




        

        
        