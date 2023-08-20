# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregar_tiquetera.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc
import icons_rc

class Ui_Dialog_agregar_tiquetera(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(612, 473)
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
"\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.central_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.choose_frame = QFrame(self.central_frame)
        self.choose_frame.setObjectName(u"choose_frame")
        self.choose_frame.setFrameShape(QFrame.StyledPanel)
        self.choose_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.choose_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.label = QLabel(self.choose_frame)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft)

        self.comboBox = QComboBox(self.choose_frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(385, 0))

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.choose_frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.num_ticket_lineEdit = QLineEdit(self.choose_frame)
        self.num_ticket_lineEdit.setObjectName(u"num_ticket_lineEdit")
        self.num_ticket_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.num_ticket_lineEdit, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.choose_frame)

        self.data_frame = QFrame(self.central_frame)
        self.data_frame.setObjectName(u"data_frame")
        self.data_frame.setStyleSheet(u"/* Estilo para QDateEdit */\n"
"QDateEdit {\n"
"    font-size: 14px;\n"
"    color: rgb(50, 50, 50);\n"
"    background-color: rgb(240, 240, 240);\n"
"    border: 2px solid rgb(173, 216, 230);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    \n"
"}\n"
"\n"
"/* Estilo para el bot\u00f3n de selecci\u00f3n de fecha */\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse sobre el QDateEdit */\n"
"QDateEdit:hover {\n"
"    border: 2px solid rgb(150, 200, 220);\n"
"}\n"
"")
        self.data_frame.setFrameShape(QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.data_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.val_day_lineEdit = QLineEdit(self.data_frame)
        self.val_day_lineEdit.setObjectName(u"val_day_lineEdit")
        self.val_day_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.val_day_lineEdit, 2, 1, 1, 1)

        self.name_label_2 = QLabel(self.data_frame)
        self.name_label_2.setObjectName(u"name_label_2")

        self.gridLayout_2.addWidget(self.name_label_2, 1, 0, 1, 1)

        self.name_label = QLabel(self.data_frame)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_2.addWidget(self.name_label, 0, 0, 1, 1, Qt.AlignLeft)

        self.start_dateEdit = QDateEdit(self.data_frame)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setMinimumSize(QSize(125, 0))
        self.start_dateEdit.setMaximumSize(QSize(800, 16777215))

        self.gridLayout_2.addWidget(self.start_dateEdit, 0, 1, 1, 1)

        self.name_label_4 = QLabel(self.data_frame)
        self.name_label_4.setObjectName(u"name_label_4")

        self.gridLayout_2.addWidget(self.name_label_4, 3, 0, 1, 1)

        self.val_all_lineEdit = QLineEdit(self.data_frame)
        self.val_all_lineEdit.setObjectName(u"val_all_lineEdit")
        self.val_all_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.val_all_lineEdit, 3, 1, 1, 1)

        self.end_dateEdit = QDateEdit(self.data_frame)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.end_dateEdit, 0, 2, 1, 1)

        self.num_days_lineEdit = QLineEdit(self.data_frame)
        self.num_days_lineEdit.setObjectName(u"num_days_lineEdit")
        self.num_days_lineEdit.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.num_days_lineEdit, 1, 1, 1, 1)

        self.name_label_3 = QLabel(self.data_frame)
        self.name_label_3.setObjectName(u"name_label_3")

        self.gridLayout_2.addWidget(self.name_label_3, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.data_frame, 0, Qt.AlignLeft)

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
        self.label.setText(QCoreApplication.translate("Dialog", u"Cliente:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Tiquetera #", None))
        self.name_label_2.setText(QCoreApplication.translate("Dialog", u"No. de comidas:", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"   Fecha \n"
"Inicio/Fin:", None))
        self.name_label_4.setText(QCoreApplication.translate("Dialog", u"Valor total:", None))
        self.name_label_3.setText(QCoreApplication.translate("Dialog", u"Valor por comida:", None))
        self.add_pushButton.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

