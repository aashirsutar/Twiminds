# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tw.ui'
#
# Created by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 288)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 321, 121))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 200, 101, 41))
        self.pushButton.setObjectName("pushButton")
#        self.label = QtGui.QLabel(Dialog)
#        self.label.setGeometry(QtCore.QRect(20, 210, 51, 21))
#        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Aashir-Twiminds", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Tweet", None, QtGui.QApplication.UnicodeUTF8))
#        self.label.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "And thou shall share :", None, QtGui.QApplication.UnicodeUTF8))

