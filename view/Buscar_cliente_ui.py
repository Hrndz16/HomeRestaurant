# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscar_cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import icons_rc
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(302, 280)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuBar_frame_2 = QFrame(Dialog)
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
        self.horizontalLayout_5.setContentsMargins(9, 11, 15, 0)

        self.verticalLayout.addWidget(self.menuBar_frame_2)

        self.central_frame = QFrame(Dialog)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"QFrame#central_frame{\n"
"	border: 3px solid rgb(173, 216, 230); /* Bordes gruesos de color RGB(173, 216, 230) */\n"
"    background-color: rgb(240, 240, 240)\n"
"}\n"
"\n"
"/* Estilo para QLabel */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(240, 240, 240);\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Estilo para QPushButton */\n"
"QPushButton {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(173, 216, 230);\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse sobre el bot\u00f3n */\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 200, 220);\n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(130, 180, 200);\n"
"}\n"
"/* Estilo para QLineEdit */\n"
"QLineEdit {\n"
"    font-size: 14px;\n"
"    color: rgb(50, 50, 50);\n"
"    background-color:"
                        " rgb(240, 240, 240);\n"
"    border: 2px solid rgb(173, 216, 230);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse sobre el QLineEdit */\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(150, 200, 220);\n"
"}\n"
"\n"
"/* Efecto al estar enfocado en el QLineEdit */\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(50, 150, 220);\n"
"}\n"
"")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.data_frame = QFrame(self.central_frame)
        self.data_frame.setObjectName(u"data_frame")
        self.data_frame.setFrameShape(QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.data_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.name_label = QLabel(self.data_frame)
        self.name_label.setObjectName(u"name_label")

        self.verticalLayout_4.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(self.data_frame)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.verticalLayout_4.addWidget(self.name_lineEdit)


        self.verticalLayout_2.addWidget(self.data_frame)

        self.buttons_frame = QFrame(self.central_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_pushButton = QPushButton(self.buttons_frame)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.horizontalLayout.addWidget(self.add_pushButton)

        self.cancel_pushButton = QPushButton(self.buttons_frame)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")

        self.horizontalLayout.addWidget(self.cancel_pushButton)


        self.verticalLayout_2.addWidget(self.buttons_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"Digite la cedula del usuario:", None))
        self.add_pushButton.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

