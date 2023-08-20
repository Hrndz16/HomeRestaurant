from view.agregar_cliente_ui import Ui_Dialog_agregar_cliente
from controllers.clases_Restaurante import Programa
from PySide6.QtWidgets import QDialog,QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap,QIntValidator
import os

class DialogAgregarCliente(QDialog, Ui_Dialog_agregar_cliente):
    
    def __init__(self,lista=Programa()):
        super().__init__()
        self.setupUi(self)
        self.menuBar_frame_2.mouseMoveEvent = self.moveWindow
        self.cancel_pushButton.clicked.connect(lambda: self.close())
        self.change_pictur_botton.clicked.connect(self.open_file_dialog)
        self.cc_lineEdit.setValidator(QIntValidator())
        self.lista = lista
        self.file_name= os.path.join('assets','icons','icons8-usuario-80.png')
        self.pixmap = QPixmap(self.file_name)
        
        

        
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        self.file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*)", options=options)

        if self.file_name:
            pixmap = QPixmap(self.file_name) 
            self.picture_label.setPixmap(pixmap)

    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
    def moveWindow(self,event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()