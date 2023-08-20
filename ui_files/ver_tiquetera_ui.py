# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ver_tiquetera.ui'
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
    QHeaderView, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import icons_rc
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(494, 471)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_3 = QVBoxLayout(self.central_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.user_tableView = QTableView(self.central_frame)
        self.user_tableView.setObjectName(u"user_tableView")

        self.verticalLayout_3.addWidget(self.user_tableView)

        self.buttons_frame = QFrame(self.central_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editar_pushButton = QPushButton(self.buttons_frame)
        self.editar_pushButton.setObjectName(u"editar_pushButton")

        self.horizontalLayout.addWidget(self.editar_pushButton, 0, Qt.AlignHCenter)

        self.cancel_pushButton = QPushButton(self.buttons_frame)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setMinimumSize(QSize(157, 0))
        self.cancel_pushButton.setMaximumSize(QSize(157, 16777215))

        self.horizontalLayout.addWidget(self.cancel_pushButton, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.buttons_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.editar_pushButton.setText(QCoreApplication.translate("Dialog", u"Editar Tiquetera", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Salir", None))
    # retranslateUi

