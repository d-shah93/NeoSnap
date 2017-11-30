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
from PyQt5.QtWidgets import QApplication
from PIL import Image
# This is our window from QtCreator
from threading import Thread
import threading
import imghdr
import picamera
import time
import datetime
import mainwindow_auto
import secondwindow_auto
import dropbox
import os
from os.path import exists
import DropboxAPI
import strandtest
from neopixel import *
import RPi.GPIO as GPIO

LED_COUNT      = 44      # Number of LED pixels was 120.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


token = 'iXbb2YaVfCAAAAAAAAAADOLjMyg5FGJw6coQnbpyLG7-mqGFG0SGZR6I1L722gzd'             
        
def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)
def rainbowCycle(strip, wait_ms=100, iterations=1):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)
		
def white(strip):
        strip.show()
        for i in range(0,46):
                strip.setPixelColor(i,Color(255,255,255))
        strip.show()
        time.sleep(1)

def clear(strip):
        strip.show()
        for i in range(0,46):
                strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(1)

def theaterChase(strip, color, wait_ms=600, iterations=1):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
class myThread(threading.Thread):
        def __init__(self):
                threading.Thread.__init__(self)
                self.strip  = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP) 
                self.strip.begin()
                self.daemon = True
                self.pause = False
                self.state = threading.Condition()
	        self.begining = True
        def run(self):
                while self.begining is True:
                        while self.pause is False:
                                theaterChase(self.strip, Color(240,70,1))
        def stahp(self):
                self.pause = True
	def stahp2(self):
		self.begining = False
		self.pause = True
        def strat(self):
                self.pause = False


class PreviewWindow(QMainWindow, secondwindow_auto.Ui_SecondWindow):
    def __init__(self,parent = None):
        super(PreviewWindow,self).__init__(parent)
        self.setupUi(self)
        self.partnerwindow = parent
        self.filename = 'default'
        self.logo = 'default'
        self.pic = PyQt5.QtWidgets.QLabel(self)
        self.Loadbutton.clicked.connect(lambda: self.handleimage())
        self.Exitbutton.clicked.connect(lambda: self.close())
        self.Retakebutton.clicked.connect(lambda: self.retake())
        self.eebutton.clicked.connect(lambda: self.pressedeebutton())
        self.Uploadbutton.clicked.connect(lambda: self.pressedupload())

    def recieve_logo(self,item):
        self.logo = item
    def recieve_filename(self,item):
        self.filename = item
    def pressedeebutton(self):
	
        sys.exit()
    def pressedupload(self):
        DropboxAPI.upload(token, self.filename)
        dbx = dropbox.Dropbox(token)
	self.hide()
    def close(self):
        self.pic.clear()
        self.hide()
        
    def retake(self):
        os.remove(os.path.expanduser('/home/pi/Desktop/Picture/' + self.filename))
        self.hide()
    def handleimage(self):
        print(self.geometry().width())
        print(self.geometry().height())
        
        if self.logo.lower() != 'default':
            mimage = Image.open(os.path.expanduser('/home/pi/Desktop/Picture/' + self.filename))
            limage = Image.open(self.logo)

            wsize =  int(min(mimage.size[0],mimage.size[1]) * 0.25)
            wpercent = (wsize/float(limage.size[0]))
            hsize = int((float(limage.size[1]) * float(wpercent)))

            simage = limage.resize((wsize,hsize))
            mbox = mimage.getbbox()
            sbox = simage.getbbox()

            box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
            mimage.paste(simage,box)
            mimage.save(os.path.expanduser('/home/pi/Desktop/Picture/' + self.filename))
        
        self.pic.setScaledContents(True)
        self.pic.setPixmap(PyQt5.QtGui.QPixmap(os.path.expanduser('/home/pi/Desktop/Picture/' + self.filename)))
        self.pic.installEventFilter(self)
        self.pic.setGeometry(self.geometry().height()/2,self.geometry().width()/10,240,340)
        self.pic.show()
    
       
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        
        # Hooks for the buttons
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()
        self.thread1 = myThread()
        self.thread1.start()
        self.resx = 320  # default x resolution
        self.resy = 240  # default y resolution
        self.filename1 = 'default'
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
	self.thread1.stahp2()
	clear(self.strip)
	clear(self.strip)
	clear(self.strip)
	print('sup')
        sys.exit()
    def pressedbrowsebutton(self):
        filename = QFileDialog.getOpenFileName(self, "Open Image", "/home", "Images (*.png *.jpg *.PNG *.JPG)")
        self.partnerwindow.recieve_logo(filename[0])
    def pictureprompt(self,value):
            with picamera.PiCamera() as camera:
                    camera.resolution = (self.resx, self.resy)
                    camera.framerate = 24
                    camera.start_preview()
                    if self.Flash == 'ON':
                            self.thread2 = Thread(target = white, args = (self.strip,))
                            self.thread2.start()
		    else:
			    self.thread2 = Thread(target = clear, args = (self.strip,))
			    self.thread2.start()
                    time.sleep(self.delay)
                    today = str(datetime.datetime.today())
                    if value == 1:
                            self.filename1 = today[:19] + '.jpg'            
                            camera.capture(self.filename1)
                    elif value == 2:
                            self.filename2 = today[:19] + '.jpg'            
                            camera.capture(self.filename2)
                    else:
                            self.filename3 = today[:19] + '.jpg'            
                            camera.capture(self.filename3)
                    camera.stop_preview()
                     
    def pressedpicbutton(self):
        self.thread1.stahp()
        
        self.pictureprompt(1)

        #prompt
        
        

        self.pictureprompt(2)

        #prompt

        self.pictureprompt(3)
        
        #with picamera.PiCamera() as camera:
            #camera.resolution = (self.resx, self.resy)
            #camera.framerate = 24
            #camera.start_preview()
            #if self.Flash == 'ON':
                    #thread1 = Thread(target = white, args = (self.strip,))
                    #thread1.start()
            #time.sleep(self.delay)
            #today = str(datetime.datetime.today())
            #fileName1 = today[:19] + '.jpg'
            
            #camera.capture(fileName1)
            
            #time.sleep(self.delay)
            #today = str(datetime.datetime.today())
            #fileName2 = today[:19] + '.jpg'
            #time.sleep(self.delay)
            
            #camera.capture(fileName2)

            #time.sleep(self.delay)
            #today = str(datetime.datetime.today())
            #fileName3 = today[:19] + '.jpg'
            
            #camera.capture(fileName3)
            
            #camera.stop_preview()
            
            #self.filename1 = fileName1
           # self.filename2 = fileName2
            #self.filename3 = fileName3

        list_image = [self.filename1,self.filename2,self.filename3]
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

            
            
        today = str(datetime.datetime.today())
        name = today[:19] + '.jpg'
        new_image.save(os.path.expanduser('/home/pi/Desktop/Picture/' + name))
            
        os.remove(self.filename1)
        os.remove(self.filename2)
        os.remove(self.filename3)
            
        self.thread1.strat() 
        self.partnerwindow.recieve_filename(name)
        new_image.close()
        self.partnerwindow.setGeometry(10,10,1080,780)
        self.partnerwindow.show()
        self.partnerwindow.showFullScreen()
              
          
def main():
    filenam = '~/Desktop/Picture/'
    
    if not os.path.exists(os.path.expanduser('/home/pi/Desktop/Picture/')):
        os.makedirs(os.path.expanduser('/home/pi/Desktop/Picture/'))
        print('Hello')    
    
    # theaterChaseRainbow(strip)  
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
