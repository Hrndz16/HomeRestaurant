from view import *
from PySide6.QtCore import Qt

class general_configuracion():
    def __init__(self,ui):
        self.ui=ui
        self.remove_title_bar()
    
    def remove_title_bar(self): 
        self.ui.setAttribute(Qt.WA_TranslucentBackground,True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
        
    
    
       