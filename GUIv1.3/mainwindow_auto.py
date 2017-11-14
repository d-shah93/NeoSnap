# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Oct 28 14:00:26 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 310)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.cameraStart = QtWidgets.QPushButton(self.centralWidget)
        self.cameraStart.setEnabled(True)
        self.cameraStart.setGeometry(QtCore.QRect(150, 90, 101, 91))
        self.cameraStart.setStyleSheet(".QPushButton#cameraStart {\n"
"border-radius: 45px;\n"
"border-style: solid;\n"
"border-width:2px;\n"
"padding: 10px 10px 10px 10px;\n"
"background-color: rgba(0, 255, 227, 255);\n"
"}")
        self.cameraStart.setObjectName("cameraStart")
        self.flash = QtWidgets.QPushButton(self.centralWidget)
        self.flash.setGeometry(QtCore.QRect(-8, -9, 181, 111))
        self.flash.setStyleSheet(".QPushButton {\n"
"position: relative;\n"
"}")
        self.flash.setObjectName("flash")
        self.LEDcolors = QtWidgets.QPushButton(self.centralWidget)
        self.LEDcolors.setGeometry(QtCore.QRect(222, -9, 181, 111))
        self.LEDcolors.setAutoFillBackground(False)
        self.LEDcolors.setObjectName("LEDcolors")
        self.OverlayButton = QtWidgets.QPushButton(self.centralWidget)
        self.OverlayButton.setGeometry(QtCore.QRect(-8, 161, 171, 91))
        self.OverlayButton.setStyleSheet("")
        self.OverlayButton.setObjectName("OverlayButton")
        self.Button = QtWidgets.QPushButton(self.centralWidget)
        self.Button.setGeometry(QtCore.QRect(232, 161, 171, 91))
        self.Button.setObjectName("Button")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 403, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cameraStart.setText(_translate("MainWindow", "Snap"))
        self.flash.setText(_translate("MainWindow", "Flash\n"
"ON/OFF"))
        self.LEDcolors.setText(_translate("MainWindow", "LED Color: \n"
"Variable"))
        self.OverlayButton.setText(_translate("MainWindow", "Overlay"))
        self.Button.setText(_translate("MainWindow", "Pineapples"))

