# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dittorier.ui'
#
# Created: Sun Mar  1 03:40:04 2015
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(805, 686)
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(570, 30, 171, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
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
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(510, 250, 281, 51))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 230, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(580, 400, 111, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 310, 85, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 650, 781, 23))
        self.progressBar.setProperty("value", 24)
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
        self.comboBox = QtGui.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(570, 90, 168, 41))
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 461, 131))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 170, 461, 131))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(10, 310, 461, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.graphicsView_3 = QtGui.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 330, 461, 131))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphicsView_4 = QtGui.QGraphicsView(Dialog)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 480, 461, 131))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(10, 10, 781, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dittorier", None))
        self.commandLinkButton.setText(_translate("Dialog", "Grabar Audio", None))
        self.label_3.setText(_translate("Dialog", "Miscelanea", None))
        self.commandLinkButton_2.setText(_translate("Dialog", "Comenzar", None))
        self.pushButton_4.setText(_translate("Dialog", "Limpiar", None))
        self.label_2.setText(_translate("Dialog", "Acción", None))
        self.comboBox.setItemText(0, _translate("Dialog", " -- -- -- -- ", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Compresión", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Convolución", None))
        self.comboBox.setItemText(3, _translate("Dialog", "Reflejar", None))
        self.label.setText(_translate("Dialog", "Cantidad", None))
        self.commandLinkButton_3.setText(_translate("Dialog", "Clonar Audio", None))

