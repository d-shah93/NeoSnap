#always have this
import sys

from Tkinter import *
#this will get the qt thingy
import PyQt5
from PyQt5.QtWidgets import *

#this will import the ui, change the text to match the name of the ui file
import picamera
import time
import mainwindow_auto

#create class

class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
	#access variables inside ui file
        #this is on button use this one deep
	def pressedOnButton(self):
                #this is where pi camera comes in
                with picamera.PiCamera() as camera:
                        #resolution 
                        camera.resolution = (320,240)
                        #framerate of the feed
                        camera.framerate = 24
                        #starts the preview
                        camera.start_preview()
                        #time in seconds
                        time.sleep(2)
                        #captures the very last frame(I think timing might make this an issue?)
                        #it will take the picture but I forget if it takes the very last frame or
                        #if it will do this right after the sleep command
                        #I think it takes the very last frame after the feed ends
                        #shoulda tested this but yeah
                        camera.capture('test.jpg')
                print("Pressed ON!")
        #this is off button deep you don't have to use this one     
	def pressedOffButton(self):
		print("Pressed Off!")
		
	def __init__(self):
                super(self.__class__, self).__init__()
                self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
                #this will connect the on button to a certain task
                self.btnOn.clicked.connect(lambda: self.pressedOnButton())
                #this will connect the off button to a certan task
                self.btnOff.clicked.connect(lambda: self.pressedOffButton())

#this you don't have to mess with Deep
def main():
	#new app instance
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
