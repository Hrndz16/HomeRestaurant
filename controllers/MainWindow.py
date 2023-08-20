
from PySide6.QtWidgets import QMainWindow
from view.MainWindow2_ui import Ui_MainWindow
from view.general_configuracion import general_configuracion
from controllers.clases_Restaurante import Programa
from PySide6.QtCore import Qt
import time
from controllers.clases_Restaurante import *
from controllers.agregar_cliente import DialogAgregarCliente
from controllers.eliminar_cliente import eliminar_cliente

class MainWindowForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.listas = cargar_datos()
        super().__init__()
        self.setupUi(self)
        self.ui = general_configuracion(self)
        self.menuBar_frame.mouseMoveEvent = self.moveWindow
        self.menuBar_frame_2.mouseMoveEvent = self.moveWindow
        
        
        self.menu_1.clicked.connect(lambda: self.pages_menu.setCurrentIndex(0))
        self.menu_2.clicked.connect(lambda: self.pages_menu.setCurrentIndex(1))
        self.menu_3.clicked.connect(lambda: self.pages_menu.setCurrentIndex(2))
        self.menu_4.clicked.connect(lambda: self.pages_menu.setCurrentIndex(3))
        self.menu_5.clicked.connect(lambda: self.pages_menu.setCurrentIndex(4))
        self.menu_6.clicked.connect(lambda: self.pages_menu.setCurrentIndex(5))
        self.menu_7.clicked.connect(lambda: self.pages_menu.setCurrentIndex(6))
        
        self.minimize_botton.clicked.connect(lambda: self.showMinimized())
        self.close_botton.clicked.connect(lambda: self.close())
        self.minimize_botton_2.clicked.connect(lambda: self.showMinimized())
        self.close_botton_2.clicked.connect(lambda: self.close())
        
        self.progressBar.setVisible(False)
        self.stackedWidget.setCurrentIndex(0)
        
        self.start_botton.clicked.connect(self.start)
        
        self.pages_menu.setCurrentIndex(0)

        self.custumer_add_botton.clicked.connect(self.openAgregar_cliente)
        self.custumer_del_botton.clicked.connect(self.openEliminar_cliente)
    
    def openEliminar_cliente(self):
        dialog = eliminar_cliente(self.listas)
        general_configuracion(dialog)
        dialog.exec()

    def openAgregar_cliente(self):
        dialog = DialogAgregarCliente(self.listas)
        general_configuracion(dialog)
        dialog.agregar_cliente()
        dialog.exec()
        


    def start(self):
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)
        self.start_botton.setVisible(False)
        for i in range(1,101):
            self.progressBar.setValue(i)
            time.sleep(0.005)
        self.stackedWidget.setCurrentIndex(1)
        
    
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
    def moveWindow(self,event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
    
    
    def guardar_datos(self,programa):
        with open(archivo, 'wb') as f:
            pickle.dump(programa, f)
            
    def cargar_datos(self):
        ruta= os.path.join("database", "archivo.pkl")
        archivo = ruta
        try:
            with open(archivo, 'rb') as f:  # Cambio: modo 'rb' para leer binario
                programa = pickle.load(f)
                return programa
        except (FileNotFoundError, pickle.UnpicklingError):
            print(f"El archivo '{archivo}' no existe o no se puede cargar. Se creará uno nuevo.")
            programa_nuevo = Programa()
            guardar_datos(programa_nuevo)  # Crear y guardar un nuevo archivo
            return programa_nuevo
        
        
