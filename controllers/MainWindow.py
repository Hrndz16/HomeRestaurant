from PySide6.QtWidgets import QMainWindow,QWidget
from view.MainWindow2_ui import *
from view.general_configuracion import *
from PySide6.QtCore import Qt
import time

class MainWindowForm(QMainWindow,Ui_MainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = general_configuracion(self)
        self.menuBar_frame.mouseMoveEvent = self.moveWindow
        self.menuBar_frame_2.mouseMoveEvent = self.moveWindow
        
        print("hola")
        
        
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
    
    
        
