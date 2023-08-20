from view.eliminar_cliente_ui import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

class eliminar_cliente(QDialog, Ui_Dialog):
    
    def __init__(self,lista):
        super().__init__()
        self.setupUi(self)
        self.menuBar_frame_2.mouseMoveEvent = self.moveWindow
        self.cancel_pushButton.clicked.connect(lambda: self.close())
        self.lista = lista
        
    
    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
    def moveWindow(self,event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()