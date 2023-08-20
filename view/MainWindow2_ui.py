# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import title_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(899, 500)
        MainWindow.setMinimumSize(QSize(899, 500))
        MainWindow.setMaximumSize(QSize(900, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_32 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
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
"   background-image:url(:/title/pictures/background.png);\n"
"   background-repeat: no-repeat;\n"
"   background-position: center;\n"
"   border-radius: 10px;\n"
"}")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 0, 6, 4)
        self.menuBar_frame = QFrame(self.background_frame)
        self.menuBar_frame.setObjectName(u"menuBar_frame")
        self.menuBar_frame.setMinimumSize(QSize(0, 40))
        self.menuBar_frame.setMaximumSize(QSize(16777215, 40))
        self.menuBar_frame.setStyleSheet(u"QFrame#menuBar_frame{\n"
" background-color:rgb(0, 115, 115);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.menuBar_frame.setFrameShape(QFrame.StyledPanel)
        self.menuBar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menuBar_frame)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 15, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.minimize_botton = QToolButton(self.menuBar_frame)
        self.minimize_botton.setObjectName(u"minimize_botton")
        self.minimize_botton.setStyleSheet(u"QToolButton#minimize_botton{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton#minimize_botton::hover{\n"
"background-color: yellow;\n"
"\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/icons8-minimizar-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_botton.setIcon(icon)
        self.minimize_botton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimize_botton)

        self.close_botton = QToolButton(self.menuBar_frame)
        self.close_botton.setObjectName(u"close_botton")
        self.close_botton.setStyleSheet(u"QToolButton#close_botton{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton#close_botton::hover{\n"
"background-color: yellow;\n"
"\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/icons8-cerrar-ventana-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_botton.setIcon(icon1)
        self.close_botton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.close_botton)


        self.verticalLayout_3.addWidget(self.menuBar_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"QFrame#content_frame {\n"
"     background-color: rgba(173, 216, 230, 100);\n"
"	 border-radius: 10px; /* Bordes redondeados *\n"
"         }")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.content_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.image_frame = QFrame(self.content_frame)
        self.image_frame.setObjectName(u"image_frame")
        self.image_frame.setMinimumSize(QSize(307, 234))
        self.image_frame.setMaximumSize(QSize(16777215, 241))
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.image_title_label = QLabel(self.image_frame)
        self.image_title_label.setObjectName(u"image_title_label")
        self.image_title_label.setGeometry(QRect(0, 0, 301, 241))
        self.image_title_label.setPixmap(QPixmap(u":/title/pictures/IMAGE TITLE.png"))
        self.image_title_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.image_frame, 0, Qt.AlignHCenter)

        self.bottons_frame = QFrame(self.content_frame)
        self.bottons_frame.setObjectName(u"bottons_frame")
        self.bottons_frame.setMinimumSize(QSize(500, 100))
        self.bottons_frame.setMaximumSize(QSize(16777215, 100))
        self.bottons_frame.setFrameShape(QFrame.StyledPanel)
        self.bottons_frame.setFrameShadow(QFrame.Raised)
        self.start_botton = QPushButton(self.bottons_frame)
        self.start_botton.setObjectName(u"start_botton")
        self.start_botton.setGeometry(QRect(160, 30, 191, 51))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(20)
        self.start_botton.setFont(font)
        self.start_botton.setLayoutDirection(Qt.LeftToRight)
        self.start_botton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(200, 200, 200); \n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7f8c8d; /* Gris al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2c3e50; /* Color m\u00e1s oscuro al presionar */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/title/assets/icons/icons8-bot\u00f3n-de-apagado-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_botton.setIcon(icon2)
        self.start_botton.setIconSize(QSize(61, 61))
        self.start_botton.setCheckable(False)
        self.start_botton.setChecked(False)
        self.start_botton.setAutoRepeat(False)
        self.start_botton.setAutoExclusive(False)
        self.progressBar = QProgressBar(self.bottons_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 0, 341, 23))
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

        self.verticalLayout.addWidget(self.bottons_frame, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.horizontalLayout_2.addWidget(self.background_frame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background2_frame = QFrame(self.page_2)
        self.background2_frame.setObjectName(u"background2_frame")
        self.background2_frame.setFrameShape(QFrame.StyledPanel)
        self.background2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.background2_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuBar_frame_2 = QFrame(self.background2_frame)
        self.menuBar_frame_2.setObjectName(u"menuBar_frame_2")
        self.menuBar_frame_2.setMinimumSize(QSize(0, 40))
        self.menuBar_frame_2.setMaximumSize(QSize(16777215, 40))
        self.menuBar_frame_2.setStyleSheet(u"QFrame#menuBar_frame_2{\n"
"background-color: rgb(173, 216, 230);\n"
"border-top-left-radius: 10px;\n"
"}\n"
"")
        self.menuBar_frame_2.setFrameShape(QFrame.StyledPanel)
        self.menuBar_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.menuBar_frame_2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 15, 0)
        self.icon_label = QLabel(self.menuBar_frame_2)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setPixmap(QPixmap(u":/icons/assets/icons/icons8-restaurante-50.png"))

        self.horizontalLayout_5.addWidget(self.icon_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.minimize_botton_2 = QToolButton(self.menuBar_frame_2)
        self.minimize_botton_2.setObjectName(u"minimize_botton_2")
        self.minimize_botton_2.setStyleSheet(u"QToolButton#minimize_botton_2{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton#minimize_botton_2::hover{\n"
"background-color: yellow;\n"
"\n"
"\n"
"}")
        self.minimize_botton_2.setIcon(icon)
        self.minimize_botton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.minimize_botton_2)

        self.close_botton_2 = QToolButton(self.menuBar_frame_2)
        self.close_botton_2.setObjectName(u"close_botton_2")
        self.close_botton_2.setStyleSheet(u"QToolButton#close_botton_2{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QToolButton#close_botton_2::hover{\n"
"background-color: yellow;\n"
"\n"
"\n"
"}")
        self.close_botton_2.setIcon(icon1)
        self.close_botton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.close_botton_2)


        self.verticalLayout_4.addWidget(self.menuBar_frame_2)

        self.menu_frame = QFrame(self.background2_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.menu_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_bottons_frame = QFrame(self.menu_frame)
        self.menu_bottons_frame.setObjectName(u"menu_bottons_frame")
        self.menu_bottons_frame.setMinimumSize(QSize(200, 0))
        self.menu_bottons_frame.setMaximumSize(QSize(200, 16777215))
        self.menu_bottons_frame.setStyleSheet(u"QFrame#menu_bottons_frame{\n"
"background-color: rgb(173, 216, 230);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(173, 216, 230);\n"
"  border-top-left-radius: 20px;\n"
" border-bottom-left-radius: 20px;\n"
"font: 75 12pt\"Arial black\";\n"
"color: rgb(50, 50, 50);\n"
" border-color: white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
" background-color:white;\n"
" border-top-left-radius: 20px;\n"
" border-bottom-left-radius: 20px;\n"
"font: 75 12pt\"Arial black\";\n"
"color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: white;\n"
"}")
        self.menu_bottons_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_bottons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menu_bottons_frame)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.menu_1 = QPushButton(self.menu_bottons_frame)
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1.setMinimumSize(QSize(0, 60))
        self.menu_1.setMaximumSize(QSize(16777215, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/icons8-p\u00e1gina-principal-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_1.setIcon(icon3)
        self.menu_1.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_1, 0, Qt.AlignLeft)

        self.separator_label = QLabel(self.menu_bottons_frame)
        self.separator_label.setObjectName(u"separator_label")
        self.separator_label.setMinimumSize(QSize(0, 1))
        self.separator_label.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_5.addWidget(self.separator_label)

        self.menu_2 = QPushButton(self.menu_bottons_frame)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setMinimumSize(QSize(0, 60))
        self.menu_2.setMaximumSize(QSize(16777215, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/icons8-cliente-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_2.setIcon(icon4)
        self.menu_2.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_2, 0, Qt.AlignLeft)

        self.separator_label_2 = QLabel(self.menu_bottons_frame)
        self.separator_label_2.setObjectName(u"separator_label_2")
        self.separator_label_2.setMinimumSize(QSize(0, 1))
        self.separator_label_2.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_5.addWidget(self.separator_label_2)

        self.menu_3 = QPushButton(self.menu_bottons_frame)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setMinimumSize(QSize(0, 60))
        self.menu_3.setMaximumSize(QSize(16777215, 60))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/icons8-empleados-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_3.setIcon(icon5)
        self.menu_3.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_3, 0, Qt.AlignLeft)

        self.separator_label_12 = QLabel(self.menu_bottons_frame)
        self.separator_label_12.setObjectName(u"separator_label_12")
        self.separator_label_12.setMinimumSize(QSize(0, 1))
        self.separator_label_12.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_5.addWidget(self.separator_label_12)

        self.menu_4 = QPushButton(self.menu_bottons_frame)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_4.setMinimumSize(QSize(0, 60))
        self.menu_4.setMaximumSize(QSize(16777215, 60))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/icons8-boleto-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_4.setIcon(icon6)
        self.menu_4.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_4, 0, Qt.AlignLeft)

        self.separator_label_13 = QLabel(self.menu_bottons_frame)
        self.separator_label_13.setObjectName(u"separator_label_13")
        self.separator_label_13.setMinimumSize(QSize(0, 1))
        self.separator_label_13.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_5.addWidget(self.separator_label_13)

        self.menu_5 = QPushButton(self.menu_bottons_frame)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_5.setMinimumSize(QSize(0, 60))
        self.menu_5.setMaximumSize(QSize(16777215, 60))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/icons8-peque\u00f1a-empresa-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_5.setIcon(icon7)
        self.menu_5.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_5)

        self.separator_label_11 = QLabel(self.menu_bottons_frame)
        self.separator_label_11.setObjectName(u"separator_label_11")
        self.separator_label_11.setMinimumSize(QSize(0, 1))
        self.separator_label_11.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_5.addWidget(self.separator_label_11)

        self.menu_6 = QPushButton(self.menu_bottons_frame)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_6.setMinimumSize(QSize(0, 60))
        self.menu_6.setMaximumSize(QSize(16777215, 60))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/icons8-producto-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_6.setIcon(icon8)
        self.menu_6.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_6, 0, Qt.AlignLeft)

        self.separator_label_7 = QLabel(self.menu_bottons_frame)
        self.separator_label_7.setObjectName(u"separator_label_7")
        self.separator_label_7.setMinimumSize(QSize(0, 1))
        self.separator_label_7.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_5.addWidget(self.separator_label_7)

        self.menu_7 = QPushButton(self.menu_bottons_frame)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_7.setMinimumSize(QSize(0, 60))
        self.menu_7.setMaximumSize(QSize(16777215, 60))
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/icons8-cuentas-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_7.setIcon(icon9)
        self.menu_7.setIconSize(QSize(61, 61))

        self.verticalLayout_5.addWidget(self.menu_7)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.menu_bottons_frame)

        self.pages_menu = QStackedWidget(self.menu_frame)
        self.pages_menu.setObjectName(u"pages_menu")
        self.inicio_page = QWidget()
        self.inicio_page.setObjectName(u"inicio_page")
        self.horizontalLayout_6 = QHBoxLayout(self.inicio_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.background_color = QFrame(self.inicio_page)
        self.background_color.setObjectName(u"background_color")
        self.background_color.setStyleSheet(u"background-color: rgb(255, 192, 203);")
        self.background_color.setFrameShape(QFrame.StyledPanel)
        self.background_color.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.background_color)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.background_image = QFrame(self.background_color)
        self.background_image.setObjectName(u"background_image")
        self.background_image.setStyleSheet(u"QFrame#background_image{\n"
"	\n"
"	background-image: url(:/title/pictures/IMAGE TITLE.png);\n"
"background-repeat: no-repeat;\n"
"    background-position: center;\n"
"\n"
"}")
        self.background_image.setFrameShape(QFrame.StyledPanel)
        self.background_image.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.background_image)


        self.horizontalLayout_6.addWidget(self.background_color)

        self.pages_menu.addWidget(self.inicio_page)
        self.costumer_page = QWidget()
        self.costumer_page.setObjectName(u"costumer_page")
        self.verticalLayout_6 = QVBoxLayout(self.costumer_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.background_color_2 = QFrame(self.costumer_page)
        self.background_color_2.setObjectName(u"background_color_2")
        self.background_color_2.setStyleSheet(u"QFrame#background_color_2{\n"
"background-color: rgb(173, 216, 230);\n"
"}")
        self.background_color_2.setFrameShape(QFrame.StyledPanel)
        self.background_color_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.background_color_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(self.background_color_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.seach_costumer_frame = QFrame(self.frame)
        self.seach_costumer_frame.setObjectName(u"seach_costumer_frame")
        self.seach_costumer_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 182, 193); /* Rosa Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.seach_costumer_frame.setFrameShape(QFrame.StyledPanel)
        self.seach_costumer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.seach_costumer_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Title_funcion_label_3 = QLabel(self.seach_costumer_frame)
        self.Title_funcion_label_3.setObjectName(u"Title_funcion_label_3")
        font1 = QFont()
        font1.setBold(True)
        self.Title_funcion_label_3.setFont(font1)

        self.verticalLayout_9.addWidget(self.Title_funcion_label_3, 0, Qt.AlignHCenter)

        self.custumer_search_botton = QPushButton(self.seach_costumer_frame)
        self.custumer_search_botton.setObjectName(u"custumer_search_botton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/icons/icons8-find-user-male-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custumer_search_botton.setIcon(icon10)
        self.custumer_search_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_9.addWidget(self.custumer_search_botton, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.seach_costumer_frame, 2, 0, 1, 1)

        self.del_costumer_frame = QFrame(self.frame)
        self.del_costumer_frame.setObjectName(u"del_costumer_frame")
        self.del_costumer_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(144, 238, 144); /* Verde Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.del_costumer_frame.setFrameShape(QFrame.StyledPanel)
        self.del_costumer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.del_costumer_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Title_funcion_label_2 = QLabel(self.del_costumer_frame)
        self.Title_funcion_label_2.setObjectName(u"Title_funcion_label_2")
        self.Title_funcion_label_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.Title_funcion_label_2, 0, Qt.AlignHCenter)

        self.custumer_del_botton = QPushButton(self.del_costumer_frame)
        self.custumer_del_botton.setObjectName(u"custumer_del_botton")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/icons/icons8-retire-hombre-usuario-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custumer_del_botton.setIcon(icon11)
        self.custumer_del_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_8.addWidget(self.custumer_del_botton, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.del_costumer_frame, 0, 1, 1, 1)

        self.add_costumer_frame = QFrame(self.frame)
        self.add_costumer_frame.setObjectName(u"add_costumer_frame")
        self.add_costumer_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.add_costumer_frame.setFrameShape(QFrame.StyledPanel)
        self.add_costumer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.add_costumer_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Title_funcion_label = QLabel(self.add_costumer_frame)
        self.Title_funcion_label.setObjectName(u"Title_funcion_label")
        self.Title_funcion_label.setFont(font1)

        self.verticalLayout_7.addWidget(self.Title_funcion_label, 0, Qt.AlignHCenter)

        self.custumer_add_botton = QPushButton(self.add_costumer_frame)
        self.custumer_add_botton.setObjectName(u"custumer_add_botton")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/icons/icons8-a\u00f1adir-grupo-de-usuarios-hombre-hombre-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custumer_add_botton.setIcon(icon12)
        self.custumer_add_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_7.addWidget(self.custumer_add_botton, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.add_costumer_frame, 0, 0, 1, 1)

        self.see_costumers_frame = QFrame(self.frame)
        self.see_costumers_frame.setObjectName(u"see_costumers_frame")
        self.see_costumers_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(200, 162, 200); /* Morado Suave */\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.see_costumers_frame.setFrameShape(QFrame.StyledPanel)
        self.see_costumers_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.see_costumers_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Title_funcion_label_4 = QLabel(self.see_costumers_frame)
        self.Title_funcion_label_4.setObjectName(u"Title_funcion_label_4")
        self.Title_funcion_label_4.setFont(font1)

        self.verticalLayout_10.addWidget(self.Title_funcion_label_4, 0, Qt.AlignHCenter)

        self.custumer_see_botton = QPushButton(self.see_costumers_frame)
        self.custumer_see_botton.setObjectName(u"custumer_see_botton")
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/icons/icons8-users-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custumer_see_botton.setIcon(icon13)
        self.custumer_see_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_10.addWidget(self.custumer_see_botton, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.see_costumers_frame, 2, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.background_color_2)

        self.pages_menu.addWidget(self.costumer_page)
        self.worker_page = QWidget()
        self.worker_page.setObjectName(u"worker_page")
        self.verticalLayout_12 = QVBoxLayout(self.worker_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.background_color_3 = QFrame(self.worker_page)
        self.background_color_3.setObjectName(u"background_color_3")
        self.background_color_3.setStyleSheet(u"QFrame#background_color_3{\n"
"background-color: rgba(173, 216, 230,100);\n"
"}")
        self.background_color_3.setFrameShape(QFrame.StyledPanel)
        self.background_color_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.background_color_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.background_color_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(173, 216, 230);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.seach_frame = QFrame(self.frame_3)
        self.seach_frame.setObjectName(u"seach_frame")
        self.seach_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 182, 193); /* Rosa Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.seach_frame.setFrameShape(QFrame.StyledPanel)
        self.seach_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.seach_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.Title_funcion_label_5 = QLabel(self.seach_frame)
        self.Title_funcion_label_5.setObjectName(u"Title_funcion_label_5")
        self.Title_funcion_label_5.setFont(font1)

        self.verticalLayout_13.addWidget(self.Title_funcion_label_5, 0, Qt.AlignHCenter)

        self.worker_search_botton = QPushButton(self.seach_frame)
        self.worker_search_botton.setObjectName(u"worker_search_botton")
        self.worker_search_botton.setIcon(icon10)
        self.worker_search_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_13.addWidget(self.worker_search_botton, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.seach_frame, 2, 0, 1, 1)

        self.del_frame = QFrame(self.frame_3)
        self.del_frame.setObjectName(u"del_frame")
        self.del_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(144, 238, 144); /* Verde Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.del_frame.setFrameShape(QFrame.StyledPanel)
        self.del_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.del_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.Title_funcion_label_6 = QLabel(self.del_frame)
        self.Title_funcion_label_6.setObjectName(u"Title_funcion_label_6")
        self.Title_funcion_label_6.setFont(font1)

        self.verticalLayout_14.addWidget(self.Title_funcion_label_6, 0, Qt.AlignHCenter)

        self.worker_del_botton = QPushButton(self.del_frame)
        self.worker_del_botton.setObjectName(u"worker_del_botton")
        self.worker_del_botton.setIcon(icon11)
        self.worker_del_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_14.addWidget(self.worker_del_botton, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.del_frame, 0, 1, 1, 1)

        self.add_frame = QFrame(self.frame_3)
        self.add_frame.setObjectName(u"add_frame")
        self.add_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"    background-color: rgb(220, 220, 220); /* Color de fondo (gris claro) */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.add_frame.setFrameShape(QFrame.StyledPanel)
        self.add_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.add_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Title_funcion_label_7 = QLabel(self.add_frame)
        self.Title_funcion_label_7.setObjectName(u"Title_funcion_label_7")
        self.Title_funcion_label_7.setFont(font1)

        self.verticalLayout_15.addWidget(self.Title_funcion_label_7, 0, Qt.AlignHCenter)

        self.worker_add_botton = QPushButton(self.add_frame)
        self.worker_add_botton.setObjectName(u"worker_add_botton")
        self.worker_add_botton.setIcon(icon12)
        self.worker_add_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_15.addWidget(self.worker_add_botton, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.add_frame, 0, 0, 1, 1)

        self.see_frame = QFrame(self.frame_3)
        self.see_frame.setObjectName(u"see_frame")
        self.see_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(200, 162, 200); /* Morado Suave */\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.see_frame.setFrameShape(QFrame.StyledPanel)
        self.see_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.see_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Title_funcion_label_8 = QLabel(self.see_frame)
        self.Title_funcion_label_8.setObjectName(u"Title_funcion_label_8")
        self.Title_funcion_label_8.setFont(font1)

        self.verticalLayout_16.addWidget(self.Title_funcion_label_8, 0, Qt.AlignHCenter)

        self.worker_see_botton = QPushButton(self.see_frame)
        self.worker_see_botton.setObjectName(u"worker_see_botton")
        self.worker_see_botton.setIcon(icon13)
        self.worker_see_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_16.addWidget(self.worker_see_botton, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.see_frame, 2, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_3)


        self.verticalLayout_12.addWidget(self.background_color_3)

        self.pages_menu.addWidget(self.worker_page)
        self.ticket_page = QWidget()
        self.ticket_page.setObjectName(u"ticket_page")
        self.verticalLayout_17 = QVBoxLayout(self.ticket_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.background_color_4 = QFrame(self.ticket_page)
        self.background_color_4.setObjectName(u"background_color_4")
        self.background_color_4.setStyleSheet(u"QFrame#background_color_4{\n"
"background-color: rgba(173, 216, 230,100);\n"
"}")
        self.background_color_4.setFrameShape(QFrame.StyledPanel)
        self.background_color_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.background_color_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.background_color_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(173, 216, 230);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.seach_frame_2 = QFrame(self.frame_4)
        self.seach_frame_2.setObjectName(u"seach_frame_2")
        self.seach_frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 182, 193); /* Rosa Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.seach_frame_2.setFrameShape(QFrame.StyledPanel)
        self.seach_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.seach_frame_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.Title_funcion_label_9 = QLabel(self.seach_frame_2)
        self.Title_funcion_label_9.setObjectName(u"Title_funcion_label_9")
        self.Title_funcion_label_9.setFont(font1)

        self.verticalLayout_18.addWidget(self.Title_funcion_label_9, 0, Qt.AlignHCenter)

        self.worker_search_botton_2 = QPushButton(self.seach_frame_2)
        self.worker_search_botton_2.setObjectName(u"worker_search_botton_2")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/icons/icons8-boleto-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.worker_search_botton_2.setIcon(icon14)
        self.worker_search_botton_2.setIconSize(QSize(96, 96))

        self.verticalLayout_18.addWidget(self.worker_search_botton_2, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.seach_frame_2, 2, 0, 1, 1)

        self.del_frame_2 = QFrame(self.frame_4)
        self.del_frame_2.setObjectName(u"del_frame_2")
        self.del_frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(144, 238, 144); /* Verde Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.del_frame_2.setFrameShape(QFrame.StyledPanel)
        self.del_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.del_frame_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.Title_funcion_label_10 = QLabel(self.del_frame_2)
        self.Title_funcion_label_10.setObjectName(u"Title_funcion_label_10")
        self.Title_funcion_label_10.setFont(font1)

        self.verticalLayout_19.addWidget(self.Title_funcion_label_10, 0, Qt.AlignHCenter)

        self.worker_del_botton_2 = QPushButton(self.del_frame_2)
        self.worker_del_botton_2.setObjectName(u"worker_del_botton_2")
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/icons/icons8-eliminar-boleto-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.worker_del_botton_2.setIcon(icon15)
        self.worker_del_botton_2.setIconSize(QSize(96, 96))

        self.verticalLayout_19.addWidget(self.worker_del_botton_2, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.del_frame_2, 0, 1, 1, 1)

        self.add_frame_2 = QFrame(self.frame_4)
        self.add_frame_2.setObjectName(u"add_frame_2")
        self.add_frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"    background-color: rgb(220, 220, 220); /* Color de fondo (gris claro) */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.add_frame_2.setFrameShape(QFrame.StyledPanel)
        self.add_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.add_frame_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Title_funcion_label_11 = QLabel(self.add_frame_2)
        self.Title_funcion_label_11.setObjectName(u"Title_funcion_label_11")
        self.Title_funcion_label_11.setFont(font1)

        self.verticalLayout_20.addWidget(self.Title_funcion_label_11, 0, Qt.AlignHCenter)

        self.worker_add_botton_2 = QPushButton(self.add_frame_2)
        self.worker_add_botton_2.setObjectName(u"worker_add_botton_2")
        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/icons/icons8-a\u00f1adir-entrada-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.worker_add_botton_2.setIcon(icon16)
        self.worker_add_botton_2.setIconSize(QSize(96, 96))

        self.verticalLayout_20.addWidget(self.worker_add_botton_2, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.add_frame_2, 0, 0, 1, 1)

        self.see_frame_2 = QFrame(self.frame_4)
        self.see_frame_2.setObjectName(u"see_frame_2")
        self.see_frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(200, 162, 200); /* Morado Suave */\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.see_frame_2.setFrameShape(QFrame.StyledPanel)
        self.see_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.see_frame_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Title_funcion_label_12 = QLabel(self.see_frame_2)
        self.Title_funcion_label_12.setObjectName(u"Title_funcion_label_12")
        self.Title_funcion_label_12.setFont(font1)

        self.verticalLayout_21.addWidget(self.Title_funcion_label_12, 0, Qt.AlignHCenter)

        self.worker_see_botton_2 = QPushButton(self.see_frame_2)
        self.worker_see_botton_2.setObjectName(u"worker_see_botton_2")
        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/icons/icons8-boleto-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.worker_see_botton_2.setIcon(icon17)
        self.worker_see_botton_2.setIconSize(QSize(96, 96))

        self.verticalLayout_21.addWidget(self.worker_see_botton_2, 0, Qt.AlignHCenter)


        self.gridLayout_3.addWidget(self.see_frame_2, 2, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_17.addWidget(self.background_color_4)

        self.pages_menu.addWidget(self.ticket_page)
        self.provedor_page = QWidget()
        self.provedor_page.setObjectName(u"provedor_page")
        self.verticalLayout_22 = QVBoxLayout(self.provedor_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.background_color_5 = QFrame(self.provedor_page)
        self.background_color_5.setObjectName(u"background_color_5")
        self.background_color_5.setStyleSheet(u"QFrame#background_color_5{\n"
"background-color: rgba(173, 216, 230,100);\n"
"}")
        self.background_color_5.setFrameShape(QFrame.StyledPanel)
        self.background_color_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.background_color_5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.background_color_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(173, 216, 230);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.del_frame_3 = QFrame(self.frame_5)
        self.del_frame_3.setObjectName(u"del_frame_3")
        self.del_frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(144, 238, 144); /* Verde Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.del_frame_3.setFrameShape(QFrame.StyledPanel)
        self.del_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.del_frame_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.Title_funcion_label_14 = QLabel(self.del_frame_3)
        self.Title_funcion_label_14.setObjectName(u"Title_funcion_label_14")
        self.Title_funcion_label_14.setFont(font1)

        self.verticalLayout_24.addWidget(self.Title_funcion_label_14, 0, Qt.AlignHCenter)

        self.prove_del_botton = QPushButton(self.del_frame_3)
        self.prove_del_botton.setObjectName(u"prove_del_botton")
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/icons/icons8-vendedor-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.prove_del_botton.setIcon(icon18)
        self.prove_del_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_24.addWidget(self.prove_del_botton, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.del_frame_3, 0, 1, 1, 1)

        self.add_frame_3 = QFrame(self.frame_5)
        self.add_frame_3.setObjectName(u"add_frame_3")
        self.add_frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"    background-color: rgb(220, 220, 220); /* Color de fondo (gris claro) */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.add_frame_3.setFrameShape(QFrame.StyledPanel)
        self.add_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.add_frame_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.Title_funcion_label_15 = QLabel(self.add_frame_3)
        self.Title_funcion_label_15.setObjectName(u"Title_funcion_label_15")
        self.Title_funcion_label_15.setFont(font1)

        self.verticalLayout_25.addWidget(self.Title_funcion_label_15, 0, Qt.AlignHCenter)

        self.prove_add_botton = QPushButton(self.add_frame_3)
        self.prove_add_botton.setObjectName(u"prove_add_botton")
        icon19 = QIcon()
        icon19.addFile(u":/icons/assets/icons/icons8-vendedor-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prove_add_botton.setIcon(icon19)
        self.prove_add_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_25.addWidget(self.prove_add_botton, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.add_frame_3, 0, 0, 1, 1)

        self.see_frame_3 = QFrame(self.frame_5)
        self.see_frame_3.setObjectName(u"see_frame_3")
        self.see_frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(200, 162, 200); /* Morado Suave */\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.see_frame_3.setFrameShape(QFrame.StyledPanel)
        self.see_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.see_frame_3)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.Title_funcion_label_16 = QLabel(self.see_frame_3)
        self.Title_funcion_label_16.setObjectName(u"Title_funcion_label_16")
        self.Title_funcion_label_16.setFont(font1)

        self.verticalLayout_26.addWidget(self.Title_funcion_label_16, 0, Qt.AlignHCenter)

        self.prove_see_botton = QPushButton(self.see_frame_3)
        self.prove_see_botton.setObjectName(u"prove_see_botton")
        icon20 = QIcon()
        icon20.addFile(u":/icons/assets/icons/icons8-vendedor-96 (3).png", QSize(), QIcon.Normal, QIcon.Off)
        self.prove_see_botton.setIcon(icon20)
        self.prove_see_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_26.addWidget(self.prove_see_botton, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.see_frame_3, 2, 1, 1, 1)

        self.seach_frame_3 = QFrame(self.frame_5)
        self.seach_frame_3.setObjectName(u"seach_frame_3")
        self.seach_frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 182, 193); /* Rosa Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.seach_frame_3.setFrameShape(QFrame.StyledPanel)
        self.seach_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.seach_frame_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.Title_funcion_label_13 = QLabel(self.seach_frame_3)
        self.Title_funcion_label_13.setObjectName(u"Title_funcion_label_13")
        self.Title_funcion_label_13.setFont(font1)

        self.verticalLayout_23.addWidget(self.Title_funcion_label_13, 0, Qt.AlignHCenter)

        self.prove_search_botton = QPushButton(self.seach_frame_3)
        self.prove_search_botton.setObjectName(u"prove_search_botton")
        icon21 = QIcon()
        icon21.addFile(u":/icons/assets/icons/icons8-vendedor-96 (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.prove_search_botton.setIcon(icon21)
        self.prove_search_botton.setIconSize(QSize(96, 96))

        self.verticalLayout_23.addWidget(self.prove_search_botton, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.seach_frame_3, 2, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.frame_5)


        self.verticalLayout_22.addWidget(self.background_color_5)

        self.pages_menu.addWidget(self.provedor_page)
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.verticalLayout_11 = QVBoxLayout(self.storage_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.background_color_6 = QFrame(self.storage_page)
        self.background_color_6.setObjectName(u"background_color_6")
        self.background_color_6.setStyleSheet(u"QFrame#background_color_6{\n"
"background-color: rgba(173, 216, 230,100);\n"
"}")
        self.background_color_6.setFrameShape(QFrame.StyledPanel)
        self.background_color_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.background_color_6)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.background_color_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(173, 216, 230);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.see_frame_6 = QFrame(self.frame_9)
        self.see_frame_6.setObjectName(u"see_frame_6")
        self.see_frame_6.setStyleSheet(u"QFrame{\n"
"background-color: rgb(200, 162, 200); /* Morado Suave */\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.see_frame_6.setFrameShape(QFrame.StyledPanel)
        self.see_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.see_frame_6)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.Title_funcion_label_28 = QLabel(self.see_frame_6)
        self.Title_funcion_label_28.setObjectName(u"Title_funcion_label_28")
        self.Title_funcion_label_28.setFont(font1)

        self.verticalLayout_40.addWidget(self.Title_funcion_label_28, 0, Qt.AlignHCenter)

        self.storage_see_botton_3 = QPushButton(self.see_frame_6)
        self.storage_see_botton_3.setObjectName(u"storage_see_botton_3")
        icon22 = QIcon()
        icon22.addFile(u":/icons/assets/icons/icons8-products-pile-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_see_botton_3.setIcon(icon22)
        self.storage_see_botton_3.setIconSize(QSize(96, 96))

        self.verticalLayout_40.addWidget(self.storage_see_botton_3, 0, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.see_frame_6, 2, 0, 1, 2)

        self.add_frame_7 = QFrame(self.frame_9)
        self.add_frame_7.setObjectName(u"add_frame_7")
        self.add_frame_7.setStyleSheet(u"QFrame{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"    background-color: rgb(220, 220, 220); /* Color de fondo (gris claro) */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.add_frame_7.setFrameShape(QFrame.StyledPanel)
        self.add_frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.add_frame_7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.Title_funcion_label_29 = QLabel(self.add_frame_7)
        self.Title_funcion_label_29.setObjectName(u"Title_funcion_label_29")
        self.Title_funcion_label_29.setFont(font1)

        self.verticalLayout_41.addWidget(self.Title_funcion_label_29, 0, Qt.AlignHCenter)

        self.storage_add_botton_4 = QPushButton(self.add_frame_7)
        self.storage_add_botton_4.setObjectName(u"storage_add_botton_4")
        icon23 = QIcon()
        icon23.addFile(u":/icons/assets/icons/icons8-mover-por-carretilla-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_add_botton_4.setIcon(icon23)
        self.storage_add_botton_4.setIconSize(QSize(96, 96))

        self.verticalLayout_41.addWidget(self.storage_add_botton_4, 0, Qt.AlignHCenter)


        self.gridLayout_8.addWidget(self.add_frame_7, 0, 0, 1, 2)


        self.verticalLayout_27.addWidget(self.frame_9)


        self.verticalLayout_11.addWidget(self.background_color_6)

        self.pages_menu.addWidget(self.storage_page)
        self.cont_page = QWidget()
        self.cont_page.setObjectName(u"cont_page")
        self.verticalLayout_31 = QVBoxLayout(self.cont_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.cont_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame#frame_8{\n"
"background-color: rgb(173, 216, 230);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.add_frame_6 = QFrame(self.frame_8)
        self.add_frame_6.setObjectName(u"add_frame_6")
        self.add_frame_6.setStyleSheet(u"QFrame{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 26px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"    background-color: rgb(220, 220, 220); /* Color de fondo (gris claro) */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.add_frame_6.setFrameShape(QFrame.StyledPanel)
        self.add_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.add_frame_6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Title_funcion_label_25 = QLabel(self.add_frame_6)
        self.Title_funcion_label_25.setObjectName(u"Title_funcion_label_25")
        self.Title_funcion_label_25.setFont(font1)
        

        self.verticalLayout_37.addWidget(self.Title_funcion_label_25, 0, Qt.AlignHCenter)

        self.storage_add_botton_3 = QPushButton(self.add_frame_6)
        self.storage_add_botton_3.setObjectName(u"storage_add_botton_3")
        icon24 = QIcon()
        icon24.addFile(u":/icons/assets/icons/icons8-recibo-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_add_botton_3.setIcon(icon24)
        self.storage_add_botton_3.setIconSize(QSize(96, 96))

        self.verticalLayout_37.addWidget(self.storage_add_botton_3, 0, Qt.AlignHCenter)


        self.gridLayout_7.addWidget(self.add_frame_6, 0, 0, 1, 1)

        self.del_frame_6 = QFrame(self.frame_8)
        self.del_frame_6.setObjectName(u"del_frame_6")
        self.del_frame_6.setStyleSheet(u"QFrame{\n"
"background-color: rgb(144, 238, 144); /* Verde Claro */\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 26px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Fuente en negrita */\n"
"    color: black; /* Color del texto (negro) */\n"
"    padding: 20px; /* Espaciado interno */\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid white; /* Borde blanco de 2px */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    color: white; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2); /* Fondo blanco semi-transparente al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4); /* Fondo blanco semi-transparente al presionar */\n"
"}")
        self.del_frame_6.setFrameShape(QFrame.StyledPanel)
        self.del_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.del_frame_6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.Title_funcion_label_20 = QLabel(self.del_frame_6)
        self.Title_funcion_label_20.setObjectName(u"Title_funcion_label_20")
        self.Title_funcion_label_20.setFont(font1)

        self.verticalLayout_30.addWidget(self.Title_funcion_label_20, 0, Qt.AlignHCenter)

        self.storage_del_botton_3 = QPushButton(self.del_frame_6)
        self.storage_del_botton_3.setObjectName(u"storage_del_botton_3")
        icon25 = QIcon()
        icon25.addFile(u":/icons/assets/icons/icons8-efectivo-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_del_botton_3.setIcon(icon25)
        self.storage_del_botton_3.setIconSize(QSize(96, 96))

        self.verticalLayout_30.addWidget(self.storage_del_botton_3, 0, Qt.AlignHCenter)


        self.gridLayout_7.addWidget(self.del_frame_6, 0, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.frame_8)

        self.pages_menu.addWidget(self.cont_page)

        self.horizontalLayout_3.addWidget(self.pages_menu)


        self.verticalLayout_4.addWidget(self.menu_frame)


        self.verticalLayout_2.addWidget(self.background2_frame)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_32.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.minimize_botton, self.close_botton)
        QWidget.setTabOrder(self.close_botton, self.minimize_botton_2)
        QWidget.setTabOrder(self.minimize_botton_2, self.close_botton_2)
        QWidget.setTabOrder(self.close_botton_2, self.menu_1)
        QWidget.setTabOrder(self.menu_1, self.menu_2)
        QWidget.setTabOrder(self.menu_2, self.menu_3)
        QWidget.setTabOrder(self.menu_3, self.menu_7)
        QWidget.setTabOrder(self.menu_7, self.menu_4)
        QWidget.setTabOrder(self.menu_4, self.menu_5)
        QWidget.setTabOrder(self.menu_5, self.menu_6)
        QWidget.setTabOrder(self.menu_6, self.custumer_add_botton)
        QWidget.setTabOrder(self.custumer_add_botton, self.custumer_del_botton)
        QWidget.setTabOrder(self.custumer_del_botton, self.custumer_search_botton)
        QWidget.setTabOrder(self.custumer_search_botton, self.custumer_see_botton)
        QWidget.setTabOrder(self.custumer_see_botton, self.worker_search_botton)
        QWidget.setTabOrder(self.worker_search_botton, self.worker_del_botton)
        QWidget.setTabOrder(self.worker_del_botton, self.worker_add_botton)
        QWidget.setTabOrder(self.worker_add_botton, self.worker_see_botton)
        QWidget.setTabOrder(self.worker_see_botton, self.worker_search_botton_2)
        QWidget.setTabOrder(self.worker_search_botton_2, self.worker_del_botton_2)
        QWidget.setTabOrder(self.worker_del_botton_2, self.worker_add_botton_2)
        QWidget.setTabOrder(self.worker_add_botton_2, self.worker_see_botton_2)
        QWidget.setTabOrder(self.worker_see_botton_2, self.prove_search_botton)
        QWidget.setTabOrder(self.prove_search_botton, self.prove_del_botton)
        QWidget.setTabOrder(self.prove_del_botton, self.prove_add_botton)
        QWidget.setTabOrder(self.prove_add_botton, self.prove_see_botton)
        QWidget.setTabOrder(self.prove_see_botton, self.start_botton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.pages_menu.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimize_botton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_botton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.image_title_label.setText("")
        self.start_botton.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.icon_label.setText("")
        self.minimize_botton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_botton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menu_1.setText(QCoreApplication.translate("MainWindow", u"      INICIO          ", None))
        self.separator_label.setText("")
        self.menu_2.setText(QCoreApplication.translate("MainWindow", u"   CLIENTES      ", None))
        self.separator_label_2.setText("")
        self.menu_3.setText(QCoreApplication.translate("MainWindow", u"  EMPLEADOS   ", None))
        self.separator_label_12.setText("")
        self.menu_4.setText(QCoreApplication.translate("MainWindow", u"  TIQUETERAS    ", None))
        self.separator_label_13.setText("")
        self.menu_5.setText(QCoreApplication.translate("MainWindow", u"PROVEEDORES", None))
        self.separator_label_11.setText("")
        self.menu_6.setText(QCoreApplication.translate("MainWindow", u"    INVENTARIO   ", None))
        self.separator_label_7.setText("")
        self.menu_7.setText(QCoreApplication.translate("MainWindow", u"  CONTADURIA    ", None))
        self.Title_funcion_label_3.setText(QCoreApplication.translate("MainWindow", u"BUSCAR CLIENTE", None))
        self.custumer_search_botton.setText("")
        self.Title_funcion_label_2.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR CLIENTE", None))
        self.custumer_del_botton.setText("")
        self.Title_funcion_label.setText(QCoreApplication.translate("MainWindow", u"AGREGAR CLIENTE", None))
        self.custumer_add_botton.setText("")
        self.Title_funcion_label_4.setText(QCoreApplication.translate("MainWindow", u"VER CLIENTES", None))
        self.custumer_see_botton.setText("")
        self.Title_funcion_label_5.setText(QCoreApplication.translate("MainWindow", u"BUSCAR EMPLEADOS", None))
        self.worker_search_botton.setText("")
        self.Title_funcion_label_6.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR EMPLEADOS", None))
        self.worker_del_botton.setText("")
        self.Title_funcion_label_7.setText(QCoreApplication.translate("MainWindow", u"AGREGAR EMPLEADOS", None))
        self.worker_add_botton.setText("")
        self.Title_funcion_label_8.setText(QCoreApplication.translate("MainWindow", u"VER EMPLEADOS", None))
        self.worker_see_botton.setText("")
        self.Title_funcion_label_9.setText(QCoreApplication.translate("MainWindow", u"EDITAR TIQUERA", None))
        self.worker_search_botton_2.setText("")
        self.Title_funcion_label_10.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR TIQUETERA", None))
        self.worker_del_botton_2.setText("")
        self.Title_funcion_label_11.setText(QCoreApplication.translate("MainWindow", u"AGREGAR TIQUETERA", None))
        self.worker_add_botton_2.setText("")
        self.Title_funcion_label_12.setText(QCoreApplication.translate("MainWindow", u"VER TIQUETERAS", None))
        self.worker_see_botton_2.setText("")
        self.Title_funcion_label_14.setText(QCoreApplication.translate("MainWindow", u"ELIMINAR PROVEEDOR", None))
        self.prove_del_botton.setText("")
        self.Title_funcion_label_15.setText(QCoreApplication.translate("MainWindow", u"AGREGAR PROVEEDOR", None))
        self.prove_add_botton.setText("")
        self.Title_funcion_label_16.setText(QCoreApplication.translate("MainWindow", u"VER PROVEEDOR", None))
        self.prove_see_botton.setText("")
        self.Title_funcion_label_13.setText(QCoreApplication.translate("MainWindow", u"BUSCAR PROVEEDOR", None))
        self.prove_search_botton.setText("")
        self.Title_funcion_label_28.setText(QCoreApplication.translate("MainWindow", u"VER INVENTARIO", None))
        self.storage_see_botton_3.setText("")
        self.Title_funcion_label_29.setText(QCoreApplication.translate("MainWindow", u"HACER PEDIDO", None))
        self.storage_add_botton_4.setText("")
        self.Title_funcion_label_25.setText(QCoreApplication.translate("MainWindow", u"ADMINISTRAR \n"
"    FACTURAS", None))
        self.storage_add_botton_3.setText("")
        self.Title_funcion_label_20.setText(QCoreApplication.translate("MainWindow", u"ADMINISTRAR \n"
"    SALARIOS", None))
        self.storage_del_botton_3.setText("")
    # retranslateUi

