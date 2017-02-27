from tkinter import *
import cv2
import time

refPr = []


class App:
    global refPr

    def get_image(self, camera):
        retval, im = camera.read()
        h, w, c = im.shape
        print("testing")
        print (h, w, c)
        return im

    def __init__(self, master):
        vc = cv2.VideoCapture(0)
        ramp_frames = 30
        frame = Frame(master)
        frame.pack()
        w = frame.winfo_width()
        h = frame.winfo_height()
        cv2.namedWindow("Allen is AMAZING",)
        #cv2.setWindowProperty("Deep is AMAZING", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            cv2.imshow("Allen is AMAZING", frame)
            rval, frame = vc.read()
            cv2.circle(frame, (320, 400), 25, (169, 169, 169),  3,  -1)
            key = cv2.waitKey(33)
            if (key == 115) or (key == 87):
                camera_capture = self.get_image(vc)
                name = time.strftime("%H%M%S")
                file = "C:\\Users\Allen.idea-PC\Pictures\\" + name + ".png"
                cv2.imwrite(file, camera_capture)
                print("File printed to", file)
                # del(vc)
            if key == 27:
                break
        cv2.destroyWindow("Allen IS AMAZING")

root = Tk()
app = App(root)
root.mainloop()
