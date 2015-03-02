# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dittorier.ui'
#
# Created: Sun Mar  1 20:36:18 2015
# by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

import random
from dittorier.config import PROJECT_PATH


class Ui_Dialog(object):
    def __init__(self):
        self.currentPath = PROJECT_PATH
        self.executed = False

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(805, 686)
        self.grabarAudio_CommandButton = QtGui.QCommandLinkButton(Dialog)
        self.grabarAudio_CommandButton.setGeometry(QtCore.QRect(570, 30, 171, 41))
        self.grabarAudio_CommandButton.setObjectName(_fromUtf8("grabarAudio_CommandButton"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(480, 30, 20, 601))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 630, 781, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.miscelanea_TextEdit = QtGui.QPlainTextEdit(Dialog)
        self.miscelanea_TextEdit.setGeometry(QtCore.QRect(510, 250, 281, 51))
        self.miscelanea_TextEdit.setObjectName(_fromUtf8("miscelanea_TextEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 230, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comenzar_CommandButton = QtGui.QCommandLinkButton(Dialog)
        self.comenzar_CommandButton.setGeometry(QtCore.QRect(580, 400, 111, 41))
        self.comenzar_CommandButton.setObjectName(_fromUtf8("comenzar_CommandButton"))
        self.limpiar_Button = QtGui.QPushButton(Dialog)
        self.limpiar_Button.setGeometry(QtCore.QRect(710, 310, 85, 27))
        self.limpiar_Button.setObjectName(_fromUtf8("limpiar_Button"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 650, 781, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(500, 140, 291, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(500, 340, 291, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 160, 281, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.accion_ComboBox = QtGui.QComboBox(self.layoutWidget)
        self.accion_ComboBox.setObjectName(_fromUtf8("accion_ComboBox"))
        self.accion_ComboBox.addItem(_fromUtf8(""))
        self.accion_ComboBox.addItem(_fromUtf8(""))
        self.accion_ComboBox.addItem(_fromUtf8(""))
        self.accion_ComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.accion_ComboBox)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cantidad_SpinBox = QtGui.QSpinBox(self.layoutWidget)
        self.cantidad_SpinBox.setObjectName(_fromUtf8("cantidad_SpinBox"))
        self.horizontalLayout.addWidget(self.cantidad_SpinBox)
        self.clonarAudio_CommandButton = QtGui.QCommandLinkButton(Dialog)
        self.clonarAudio_CommandButton.setGeometry(QtCore.QRect(570, 90, 168, 41))
        self.clonarAudio_CommandButton.setObjectName(_fromUtf8("clonarAudio_CommandButton"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(10, 310, 461, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(10, 10, 781, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_image_1 = QtGui.QLabel(Dialog)
        self.label_image_1.setGeometry(QtCore.QRect(10, 30, 461, 131))
        self.label_image_1.setObjectName(_fromUtf8("label_image_1"))
        self.label_image_2 = QtGui.QLabel(Dialog)
        self.label_image_2.setGeometry(QtCore.QRect(10, 180, 461, 131))
        self.label_image_2.setObjectName(_fromUtf8("label_image_2"))
        self.label_image_3 = QtGui.QLabel(Dialog)
        self.label_image_3.setGeometry(QtCore.QRect(10, 330, 461, 131))
        self.label_image_3.setObjectName(_fromUtf8("label_image_3"))
        self.label_image_4 = QtGui.QLabel(Dialog)
        self.label_image_4.setGeometry(QtCore.QRect(10, 480, 461, 131))
        self.label_image_4.setObjectName(_fromUtf8("label_image_4"))
        self.retranslateUi(Dialog)
        #
        self.grabarAudio_CommandButton.clicked.connect(self.set_signal_1)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dittorier", None))
        self.grabarAudio_CommandButton.setText(_translate("Dialog", "Grabar Audio", None))
        self.label_3.setText(_translate("Dialog", "Miscelanea", None))
        self.comenzar_CommandButton.setText(_translate("Dialog", "Comenzar", None))
        self.limpiar_Button.setText(_translate("Dialog", "Limpiar", None))
        self.label_2.setText(_translate("Dialog", "Acción", None))
        self.accion_ComboBox.setItemText(0, _translate("Dialog", " -- -- -- -- ", None))
        self.accion_ComboBox.setItemText(1, _translate("Dialog", "Compresión", None))
        self.accion_ComboBox.setItemText(2, _translate("Dialog", "Convolución", None))
        self.accion_ComboBox.setItemText(3, _translate("Dialog", "Reflejar", None))
        self.label.setText(_translate("Dialog", "Cantidad", None))
        self.clonarAudio_CommandButton.setText(_translate("Dialog", "Clonar Audio", None))

    def set_signal_1(self):
        if self.executed:
            filename = "/signal/image/signal1.png"
            image = QtGui.QImage(self.currentPath + filename)
            pp = QtGui.QPixmap.fromImage(image)
            self.label_image_1.setScaledContents(True)
            self.label_image_1.setPixmap(pp)
        else:
            messageBox = QtGui.QMessageBox()
            messageBox.setText("Es necesario ejecutar!")
            messageBox.exec_()