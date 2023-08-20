from view.agregar_cliente_ui import Ui_Dialog_agregar_cliente
from controllers.clases_Restaurante import Programa
from PySide6.QtWidgets import QDialog,QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap,QIntValidator

class DialogAgregarCliente(QDialog, Ui_Dialog_agregar_cliente):
    
    def __init__(self,lista):
        super().__init__()
        self.setupUi(self)
        self.menuBar_frame_2.mouseMoveEvent = self.moveWindow
        self.cancel_pushButton.clicked.connect(lambda: self.close())
        self.change_pictur_botton.clicked.connect(self.open_file_dialog)
        self.cc_lineEdit.setValidator(QIntValidator())
        self.lista = lista
        self.pixmap = QPixmap()
        
        
        
        
        
    def agregar_cliente(self):
        nombre = self.name_lineEdit.text()
        cedula = self.cc_lineEdit.text()
        foto=self.pixmap
        if self.normal_radioButton.isChecked():
            tipo = "Normal"
        else:
            tipo = "Preferencial"
        
        
        self.add_pushButton.clicked.connect(lambda: self.registrar_cliente(nombre,cedula,tipo,foto))
        
    def registrar_cliente(self,nombre, cedula, tipo, foto):
        self.lista.agregar_cliente(nombre, cedula, tipo, foto)
        self.close()
        
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*)", options=options)

        if file_name:
            self.pixmap = QPixmap(file_name) 
            self.picture_label.setPixmap(self.pixmap)

    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
    def moveWindow(self,event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()