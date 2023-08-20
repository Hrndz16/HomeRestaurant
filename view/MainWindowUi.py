from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 449)
        MainWindow.setMinimumSize(QSize(779, 449))
        MainWindow.setMaximumSize(QSize(779, 449))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.page)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"QFrame#background_frame {\n"
"    background-image: url(D:/Proyectos/HomeRestaurant/pictures/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	\n"
"\n"
"}\n"
"")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.background_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"QFrame#content_frame {\n"
"                background-color: rgba(173, 216, 230, 100); /* Color azul claro con transparencia */\n"
"				border-radius: 10px; /* Bordes redondeados */\n"
"            }")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.start_botton = QPushButton(self.content_frame)
        self.start_botton.setObjectName(u"start_botton")
        self.start_botton.setGeometry(QRect(280, 280, 191, 51))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(20)
        self.start_botton.setFont(font)
        self.start_botton.setLayoutDirection(Qt.LeftToRight)
        self.start_botton.setStyleSheet(u"""QPushButton#start_botton{\n
  background-color: rgba(192, 192, 192,150);\n
  border-radius: 10px; /* Bordes redondeados */\n
  color: white; /* Color del texto */\n
  border-radius: 5px; /* Bordes redondeados */\n
  padding: 10px 20px; /* Espaciado interno */\n
  text-align: left;
   padding-left: 20px; /* Ajusta el espacio a la izquierda del icono */
  padding-right: 20px; /* Ajusta el espacio a la derecha del texto */
}  

QPushButton#start_botton:pressed {
background-color: #2980b9; 
}
            
            }""")
        
        icon = QIcon()
        imagePathS = os.path.join('assets\icons' , 'Start_icon.png')
        icon.addFile(imagePathS, QSize(), QIcon.Normal, QIcon.Off)
        self.start_botton.setIcon(icon)
        self.start_botton.setIconSize(QSize(61, 61))
        self.start_botton.setCheckable(True)
        self.start_botton.setChecked(True)
        self.start_botton.setAutoRepeat(False)
        
        
        self.progressBar = QProgressBar(self.content_frame)
        self.progressBar.setObjectName("uprogressBar")
        self.progressBar.setGeometry(QRect(210, 300, 341, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid white; /* Borde blanco */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    background-color: white; /* Fondo gris */\n"
"    text-align: center; /* Centrar el texto */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: gray; /* Color de la barra de progreso */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"}\n"
"")
        self.progressBar.setValue(24)
        self.start_botton.raise_()
        self.progressBar.raise_()
        self.image_title_label = QLabel(self.content_frame)
        self.image_title_label.setObjectName(u"image_title_label")
        self.image_title_label.setGeometry(QRect(230, 30, 271, 231))
        imagePath = os.path.join('pictures' , 'IMAGE TITLE.png')
        self.image_title_label.setPixmap(QPixmap(imagePath))
        self.image_title_label.setScaledContents(True)
        self.image_title_label.raise_()
        

        self.horizontalLayout_3.addWidget(self.content_frame)


        self.horizontalLayout_2.addWidget(self.background_frame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout = QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.central2 = QFrame(self.page_2)
        self.central2.setObjectName(u"central2")
        self.central2.setFrameShape(QFrame.StyledPanel)
        self.central2.setFrameShadow(QFrame.Raised)
        self.background2_frame = QFrame(self.central2)
        self.background2_frame.setObjectName(u"background2_frame")
        self.background2_frame.setGeometry(QRect(20, 10, 759, 429))
        self.background2_frame.setStyleSheet(u"QFrame#background2_frame{\n"
"    background-image: url(D:/Proyectos/HomeRestaurant/pictures/background.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	}")
        self.background2_frame.setFrameShape(QFrame.StyledPanel)
        self.background2_frame.setFrameShadow(QFrame.Raised)
        self.menu_frame = QFrame(self.background2_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(0, 0, 171, 431))
        self.menu_frame.setStyleSheet(u"")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.background2_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(440, 110, 120, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.central2)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_botton.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.image_title_label.setText("")
    # retranslateUi

