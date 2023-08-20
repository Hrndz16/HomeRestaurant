# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_facturas.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc
import fotos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(366, 572)
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
"/* Estilo para QListWidget */\n"
"QListWidget {\n"
"    font-size: 14px;\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(240, 240, 240);\n"
"    border: 2px solid rgb(173, 216, 230);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    min-width: 150px; /* Ancho m\u00ednimo para asegurar que se vean los elementos */\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse sobre un elemento en QListWidget */\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(200, 220, 240);\n"
"}\n"
"\n"
"/* Efecto al seleccionar un elemento en QListWidget */\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(150, 200, 220);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Estilo para QLabel */\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(240, 240, 240);\n"
"    pa"
                        "dding: 10px;\n"
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
"    background-color: rgb(240, 240, 240);\n"
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
"    border: 2p"
                        "x solid rgb(50, 150, 220);\n"
"}\n"
"/* Estilo para QComboBox */\n"
"QComboBox {\n"
"    font-size: 14px;\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(240, 240, 240);\n"
"    border: 2px solid rgb(173, 216, 230);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Estilo para el desplegable del QComboBox */\n"
"QComboBox::drop-down {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse sobre el QComboBox */\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(150, 200, 220);\n"
"}\n"
"\n"
"")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.central_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttons_frame = QFrame(self.central_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(304, 0))
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.buttons_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cancel_pushButton_4 = QPushButton(self.buttons_frame)
        self.cancel_pushButton_4.setObjectName(u"cancel_pushButton_4")
        self.cancel_pushButton_4.setMinimumSize(QSize(123, 0))

        self.gridLayout_3.addWidget(self.cancel_pushButton_4, 1, 0, 1, 1)

        self.cancel_pushButton_3 = QPushButton(self.buttons_frame)
        self.cancel_pushButton_3.setObjectName(u"cancel_pushButton_3")
        self.cancel_pushButton_3.setMinimumSize(QSize(123, 0))

        self.gridLayout_3.addWidget(self.cancel_pushButton_3, 0, 0, 1, 1)

        self.cancel_pushButton = QPushButton(self.buttons_frame)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setMinimumSize(QSize(123, 0))

        self.gridLayout_3.addWidget(self.cancel_pushButton, 0, 2, 2, 1)


        self.gridLayout_2.addWidget(self.buttons_frame, 2, 0, 1, 1)

        self.frame = QFrame(self.central_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 2)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_4.addWidget(self.plainTextEdit, 1, 0, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.central_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 76))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel_pushButton_4.setText(QCoreApplication.translate("Dialog", u"Pagar Todo", None))
        self.cancel_pushButton_3.setText(QCoreApplication.translate("Dialog", u"Pagar", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Valor total ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Total de todas\n"
" Las facturas", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"No de facturas:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

