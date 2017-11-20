# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondwindow.ui'
#
# Created: Wed Nov 15 20:46:16 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(628, 369)
        self.centralWidget = QtWidgets.QWidget(SecondWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Loadbutton = QtWidgets.QPushButton(self.centralWidget)
        self.Loadbutton.setGeometry(QtCore.QRect(0, 0, 121, 31))
        self.Loadbutton.setObjectName("Loadbutton")
        self.eebutton = QtWidgets.QPushButton(self.centralWidget)
        self.eebutton.setGeometry(QtCore.QRect(0, 280, 121, 31))
        self.eebutton.setObjectName("eebutton")
        self.Exitbutton = QtWidgets.QPushButton(self.centralWidget)
        self.Exitbutton.setGeometry(QtCore.QRect(350, 0, 111, 31))
        self.Exitbutton.setObjectName("Exitbutton")
        self.Uploadbutton = QtWidgets.QPushButton(self.centralWidget)
        self.Uploadbutton.setGeometry(QtCore.QRect(120, 0, 131, 31))
        self.Uploadbutton.setObjectName("Uploadbutton")
        self.Retakebutton = QtWidgets.QPushButton(self.centralWidget)
        self.Retakebutton.setGeometry(QtCore.QRect(250, 0, 101, 31))
        self.Retakebutton.setObjectName("Retakebutton")
        SecondWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(SecondWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 628, 20))
        self.menuBar.setObjectName("menuBar")
        SecondWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(SecondWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        SecondWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(SecondWindow)
        self.statusBar.setObjectName("statusBar")
        SecondWindow.setStatusBar(self.statusBar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.Loadbutton.setText(_translate("SecondWindow", "Preview Image"))
        self.eebutton.setText(_translate("SecondWindow", "Emergency Exit"))
        self.Exitbutton.setText(_translate("SecondWindow", "Exit"))
        self.Uploadbutton.setText(_translate("SecondWindow", "Upload To Dropbox"))
        self.Retakebutton.setText(_translate("SecondWindow", "Re-Take Pic"))

