# always seem to need this
from __future__ import print_function
import string;print(string.__file__)
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# This is our window from QtCreator
import picamera
import time
import datetime
import mainwindow_auto
import dropbox
import os
import DropboxAPI


token = 'i0Uyu-jWN94AAAAAAAANb0HoXUi4GvgcnmEunB0sZwSUgME7p7eWEmCTgYRqgoR5'
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        # Hooks for the buttons
        self.resx = 320  # default x resolution
        self.resy = 240  # default y resolution
        self.filename = 'default'
        self.pngpath = 'default'
        self.delay = 2
        filename = self.Picbtn.clicked.connect(lambda: self.pressedpicbutton())
        self.Resbox.activated.connect(lambda: self.pressedresbox())
        self.EntrBtn.clicked.connect(lambda: self.pressedenterbutton())
        self.Delay.editingFinished.connect(lambda: self.entereddelay())
        self.browseBtn.clicked.connect(lambda: self.pressedbrowsebutton())

    def pressedbrowsebutton(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        if dlg.exec_():
            print("success")
            filenames = dlg.selectedFiles()
            print(filenames)
            self.pngfile = filenames
            
            
    def entereddelay(self):
        self.delay = int(self.Delay.text())
        
    def pressedenterbutton(self):
        print(self.filename)
        # dropbox API currently using Deep's token
        # I better not see dick pics in my dropbox!!!

        DropboxAPI.upload(token, self.filename)
        dbx = dropbox.Dropbox(token)

    def pressedpicbutton(self):
        with picamera.PiCamera() as camera:
            # resolution
            camera.resolution = (self.resx, self.resy)
            # framerate of the feed
            camera.framerate = 24
            # starts the preview
            camera.start_preview()
            # time in seconds
            time.sleep(self.delay)
            # captures the very last frame(I think timing might make this an issue?)
            # it will take the picture but I forget if it takes the very last frame or
            # if it will do this right after the sleep command
            # I think it takes the very last frame after the feed ends
            # shoulda tested this but yeah

            today = str(datetime.datetime.today())
            #inTab = " -:"
            #outTab = "_11"
            #transTable = str.maketrans(inTab, outTab)
            #today = today.translate(transTable)
            fileName = today[:19] + '.jpg'
            camera.capture(fileName)
            camera.stop_preview()
            self.filename = fileName
        # access variables inside of the UI's file
            return fileName

    def pressedresbox(self):
        print(self.Resbox.currentIndex())
        index = self.Resbox.currentIndex()
        # sets the resoluton according to the drop down index
        if index == 0:
            self.resx = 500
            self.resy = 480
        elif index == 1:
            self.resx = 720
            self.resy = 480
        elif index == 2:
            self.resx = 720
            self.resy = 576
        elif index == 3:
            self.resx = 1280
            self.resy = 720
        elif index == 4:
            self.resx = 1440
            self.resy = 1080
        elif index == 5:
            self.resx = 1920
            self.resy = 1080
        else:
            print("serious Error!")
        print(self.resx)
        print(self.resy)


# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
