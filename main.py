from tkinter import *
import cv2
import time

class App:
    def get_image(self, camera):
        retval, im = camera.read()
        h, w, c = im.shape
        print("testing")
        print (h, w, c)
        print ('testing')

        return im

    def __init__(self, master):
        vc = cv2.VideoCapture(0)
        ramp_frames = 30
        frame = Frame(master)
        frame.pack()
        w = frame.winfo_width()
        h = frame.winfo_height()
        cv2.namedWindow("Deep is AMAZING",)
        #cv2.setWindowProperty("Deep is AMAZING", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            cv2.imshow("Deep is AMAZING", frame)
            rval, frame = vc.read()
            cv2.circle(frame, (320, 400), 25, (169, 169, 169),  3,  -1)
            key = cv2.waitKey(20)
            if (key == 115) or (key == 87):
                camera_capture = self.get_image(vc)
                name = time.strftime("%H%M%S")
                file = "C:\\Users\deepshah\Documents\GitHub\Photobooth\Pictures\\"  + name + ".png"
                cv2.imwrite(file, camera_capture)
                print("File printed to %s", file)
                #del(vc)
            if key == 27:
                break
        cv2.destroyWindow("Deep IS AMAZING")

root = Tk()
app = App(root)
root.mainloop()

# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.overrideredirect(1)
# root.geometry("%dx%d+0+0" % (w,h))
# root.configure(background='black')
# app = App(root)
# root.mainloop()
# root.destroy()