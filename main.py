from tkinter import *
import cv2

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        cv2.namedWindow("Deep is AMAZING",cv2.WND_PROP_FULLSCREEN)
        vc = cv2.VideoCapture(0)
        cv2.setWindowProperty("Deep is AMAZING", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            cv2.imshow("Deep is AMAZING", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:
                break
        cv2.destroyWindow("Deep IS AMAZING")
root = Tk()
app = App(root)
root.mainloop()




#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
#root.geometry("%dx%d+0+0" % (w,h))
#root.configure(background='black')
#app = App(root)

#root.mainloop()
#root.destroy()
