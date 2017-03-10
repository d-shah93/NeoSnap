from tkinter import *
import cv2
import argparse
import time


# global event
class App:
    # this function grabs the image from the camera
    def get_image(self, camera):
        retval, im = camera.read()
        h, w, c = im.shape
        print("This is from the Raspberry Pi.")
        print(h, w, c)
        return im

    def __init__(self, master):
        # this function will register mouse click
        def register_click(event, x, y, flags, param):
            # check to see if left mouse button was clicked
            if event == cv2.EVENT_LBUTTONDOWN:
                # x,y represent coordinate for the mouse
                print
                x, y
                # check to see if the click is inside the circle button
                if 295 <= x <= 345 and 375 <= y <= 425:
                    camera_capture = self.get_image(vc)
                    name = time.strftime("%H%M%S")
                    # make sure to change this right now it's for my(hemant)directory
                    file = "/home/hemant/Pictures" + name + ".png"
                    cv2.imwrite(file, camera_capture)
                    print("File printed to %s", file)

        vc = cv2.VideoCapture(0)
        ramp_frames = 30  # fps
        frame = Frame(master)
        frame.pack()
        w = frame.winfo_width()
        h = frame.winfo_height()
        cv2.namedWindow("Deep is AMAZING", )
        # cv2.setWindowProperty("Deep is AMAZING", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            # refPt = 0,0
            # creates window frame with deep is amazing as the window name
            cv2.imshow("Deep is AMAZING", frame)
            rval, frame = vc.read()
            # create the circle button, with 320,400 as midpoint and 25 radius
            cv2.circle(frame, (320, 400), 25, (169, 169, 169), 3, -1)
            # checks to see if the button was clicked in the deep is amazing window
            cv2.setMouseCallback("Deep is AMAZING", register_click)
            key = cv2.waitKey(20)

            # refPt
            # if (key == 115)  :
            #   camera_capture = self.get_image(vc)
            #  name = time.strftime("%H%M%S")
            #  file = "/home/hemant/Pictures"  + name + ".png"
            #  cv2.imwrite(file, camera_capture)
            #  print("File printed to %s", file)
            # del(vc)
            if key == 27:   #esc key
                break
        cv2.destroyWindow("Deep IS AMAZING")


root = Tk()
app = App(root)
root.mainloop()

# <<<<<<< HEAD



# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.overrideredirect(1)
# root.geometry("%dx%d+0+0" % (w,h))
# root.configure(background='black')
# app = App(root)

# root.mainloop()
# root.destroy()
# =======
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.overrideredirect(1)
# root.geometry("%dx%d+0+0" % (w,h))
# root.configure(background='black')
# app = App(root)
# root.mainloop()
# root.destroy()
# >>>>>>> c041f0cdf39bec4fbcf998f1363008996e52d852
