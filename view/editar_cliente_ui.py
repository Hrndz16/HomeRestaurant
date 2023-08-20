# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_cliente.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
import icons_rc
import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(342, 513)
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
        self.picture_frame = QFrame(self.central_frame)
        self.picture_frame.setObjectName(u"picture_frame")
        self.picture_frame.setFrameShape(QFrame.StyledPanel)
        self.picture_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.picture_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.picture_label = QLabel(self.picture_frame)
        self.picture_label.setObjectName(u"picture_label")
        self.picture_label.setStyleSheet(u"border: 5px solid rgb(173, 216, 230); /* Borde de color RGB(173, 216, 230) */\n"
"    padding: 5px; /* Espaciado interno para separar el contenido del borde */")
        self.picture_label.setPixmap(QPixmap(u":/icons/assets/icons/icons8-usuario-80.png"))

        self.verticalLayout_3.addWidget(self.picture_label, 0, Qt.AlignHCenter)

        self.change_pictur_botton = QPushButton(self.picture_frame)
        self.change_pictur_botton.setObjectName(u"change_pictur_botton")
        self.change_pictur_botton.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change_pictur_botton.setIcon(icon)
        self.change_pictur_botton.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.change_pictur_botton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.picture_frame)

        self.data_frame = QFrame(self.central_frame)
        self.data_frame.setObjectName(u"data_frame")
        self.data_frame.setFrameShape(QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.data_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cc_label = QLabel(self.data_frame)
        self.cc_label.setObjectName(u"cc_label")

        self.gridLayout_2.addWidget(self.cc_label, 2, 0, 1, 1)

        self.name_label = QLabel(self.data_frame)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_2.addWidget(self.name_label, 0, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.data_frame)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.gridLayout_2.addWidget(self.name_lineEdit, 0, 1, 1, 1)

        self.cc_lineEdit = QLineEdit(self.data_frame)
        self.cc_lineEdit.setObjectName(u"cc_lineEdit")

        self.gridLayout_2.addWidget(self.cc_lineEdit, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.data_frame)

        self.stats_frame = QFrame(self.central_frame)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setFrameShape(QFrame.StyledPanel)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.stats_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.normal_label = QLabel(self.stats_frame)
        self.normal_label.setObjectName(u"normal_label")

        self.gridLayout.addWidget(self.normal_label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.pro_label = QLabel(self.stats_frame)
        self.pro_label.setObjectName(u"pro_label")

        self.gridLayout.addWidget(self.pro_label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.pro_radioButton = QRadioButton(self.stats_frame)
        self.pro_radioButton.setObjectName(u"pro_radioButton")

        self.gridLayout.addWidget(self.pro_radioButton, 1, 1, 1, 1, Qt.AlignHCenter)

        self.normal_radioButton = QRadioButton(self.stats_frame)
        self.normal_radioButton.setObjectName(u"normal_radioButton")

        self.gridLayout.addWidget(self.normal_radioButton, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.stats_frame)

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
        self.picture_label.setText("")
        self.change_pictur_botton.setText(QCoreApplication.translate("Dialog", u"Subir Foto", None))
        self.cc_label.setText(QCoreApplication.translate("Dialog", u"Cedula:", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.normal_label.setText(QCoreApplication.translate("Dialog", u"Cliente Normal", None))
        self.pro_label.setText(QCoreApplication.translate("Dialog", u"Cliente Preferencial", None))
        self.pro_radioButton.setText("")
        self.normal_radioButton.setText("")
        self.add_pushButton.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

