#!/usr/local/bin/python
#!/usr/bin/env python

# always seem to need this
from __future__ import print_function
import string;print(string.__file__)
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image
# This is our window from QtCreator
import imghdr
import picamera
import time
import datetime
import mainwindow_auto
import secondwindow_auto
import dropbox
import os
import DropboxAPI


token = 'i0Uyu-jWN94AAAAAAAANb0HoXUi4GvgcnmEunB0sZwSUgME7p7eWEmCTgYRqgoR5'
class PreviewWindow(QMainWindow, secondwindow_auto.Ui_SecondWindow):
    def __init__(self,parent = None):
        super(PreviewWindow,self).__init__(parent)
        self.setupUi(self)
        self.partnerwindow = parent
        self.filename = 'default'
        self.logo = 'default'
        self.Loadbutton.clicked.connect(lambda: self.handleimage())
        self.Exitbutton.clicked.connect(lambda: self.close())
        self.Retakebutton.clicked.connect(lambda: self.retake())
        self.eebutton.clicked.connect(lambda: self.pressedbrowsebutton())
        self.Uploadbutton.clicked.connect(lambda: self.pressedupload())

    def recieve_logo(self,item):
        self.logo = item
    def recieve_filename(self,item):
        self.filename = item
        
    def pressedupload(self):
        DropboxAPI.upload(token, self.filename)
        dbx = dropbox.Dropbox(token)
    def close(self):
        
        self.hide()
        
    def retake(self):
        os.remove(os.path.expanduser('~/Desktop/Picture/' + self.filename))
        self.hide()
    def handleimage(self):
        print(self.geometry().width())
        print(self.geometry().height())
        
        if self.logo.lower() != 'default':
            mimage = Image.open(os.path.expanduser('~/Desktop/Picture/' + self.filename))
            limage = Image.open(self.logo)

            wsize =  int(min(mimage.size[0],mimage.size[1]) * 0.25)
            wpercent = (wsize/float(limage.size[0]))
            hsize = int((float(limage.size[1]) * float(wpercent)))

            simage = limage.resize((wsize,hsize))
            mbox = mimage.getbbox()
            sbox = simage.getbbox()

            box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
            mimage.paste(simage,box)
            mimage.save(os.path.expanduser('~/Desktop/Picture/' + self.filename))
        self.pic = PyQt5.QtWidgets.QLabel(self)
        self.pic.setScaledContents(True)
        self.pic.setPixmap(PyQt5.QtGui.QPixmap(os.path.expanduser('~/Desktop/Picture/' + self.filename)))
        self.pic.installEventFilter(self)
        self.pic.setGeometry(self.geometry().height()/2,self.geometry().width()/10,240,340)
        self.pic.show()
    
       
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        # Hooks for the buttons
        self.resx = 320  # default x resolution
        self.resy = 240  # default y resolution
        self.filenam1 = 'default'
        self.filename2 = 'default'
        self.filename3 = 'default'
        self.pngpath = 'default'
        self.png = 'PNG'
        self.jpeg = 'JPEG'
        self.delay = 2
        self.Flash = 'OFF'
        self.partnerwindow = PreviewWindow(self)
        self.cameraStart.clicked.connect(lambda: self.pressedpicbutton())
        self.OverlayButton.clicked.connect(lambda: self.pressedbrowsebutton())
        self.exitButton.clicked.connect(lambda: self.emergencybutton())
        self.flash.clicked.connect(lambda: self.flashcall())
    def flashcall(self):
        if self.Flash == 'OFF':
            self.Flash = 'ON'
            self.flash.setText('ON')
        else:
            self.Flash = 'OFF'
            self.flash.setText('OFF')
        print(self.Flash)
    def emergencybutton(self):
        sys.exit()
    def pressedbrowsebutton(self):
        filename = QFileDialog.getOpenFileName(self, "Open Image", "/home", "Images (*.png *.jpg *.PNG *.JPG)")
        self.partnerwindow.recieve_logo(filename[0])
           
    def pressedpicbutton(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (self.resx, self.resy)
            camera.framerate = 24
            camera.start_preview()
            
            time.sleep(self.delay)
            today = str(datetime.datetime.today())
            fileName1 = today[:19] + '.jpg'
            camera.capture(fileName1)
            
            time.sleep(self.delay)
            today = str(datetime.datetime.today())
            fileName2 = today[:19] + '.jpg'
            time.sleep(self.delay)
            camera.capture(fileName2)

            time.sleep(self.delay)
            today = str(datetime.datetime.today())
            fileName3 = today[:19] + '.jpg'
            camera.capture(fileName3)
            
            camera.stop_preview()
            
            self.filename1 = fileName1
            self.filename2 = fileName2
            self.filename3 = fileName3

            #list_image = [self.filename1,self.filename2,self.filename3]
            list_image = map(Image.open,[self.filename1,self.filename2,self.filename3])
            widths, heights = zip(*(i.size for i in list_image))
        
            total_width = max(widths)
            max_height = sum(heights)
        
            new_image  = Image.new('RGB',(total_width,max_height))
            y_offset = 0
            x_offset = 0
            for elem in list_image:
                print(elem)
                new_image.paste(elem,(0,y_offset))
                y_offset += elem.size[1]

            os.remove(self.filename1)
            os.remove(self.filename2)
            os.remove(self.filename3)
            
            today = str(datetime.datetime.today())
            name = today[:19] + '.jpg'
            new_image.save(os.path.expanduser('~/Desktop/Picture/' + name))
            
           
            self.partnerwindow.recieve_filename(name)
            new_image.close()
            self.partnerwindow.setGeometry(10,10,1080,780)
            self.partnerwindow.show()
            self.partnerwindow.showFullScreen()
            
def main():
    filenam = 'default'
    if not os.path.exists(os.path.expanduser('~/Desktop/Picture/')):
        os.makedirs(os.path.expanduser('~/Desktop/Picture/'))
        
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    #form.showFullScreen()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
