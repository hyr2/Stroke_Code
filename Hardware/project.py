try:
    import Tkinter as tk
except:
    import tkinter as tk

from PIL import Image, ImageTk
from matplotlib import image
import numpy as np
from matplotlib import pyplot as plt
import cv2, logging, matplotlib
from screeninfo import get_monitors
from roipoly import MultiRoi
# import pyfirmata
import time


class Test():
    def __init__(self,image_input,w,h):
        self.image_main = image_input
        self.root = tk.Tk()
        x = 0
        y = 0
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.attributes('-fullscreen', True)         # method 1 for true full screen
        # self.root.overrideredirect(True)                  # method 2 for true full screen     
        imgtk = ImageTk.PhotoImage(image=self.image_main)  # converting PIL image to PhotoImage compatible with tkinter
        Panel = tk.Label(self.root, image = imgtk).pack()
        # Quit button
        # button = tk.Button(self.root, text = 'Quit', command=self.quit)
        # button.pack()
        # Press escape to quit
        self.root.bind("<Escape>", self.quit)
        # get screen width and height
		# ws = root.winfo_screenwidth() # width of the screen
		# hs = root.winfo_screenheight() # height of the screen
        self.root.mainloop()

    def quit(self, event):
        # board.digital[2].write(0)
        # board.digital[3].write(0)
        self.root.destroy()

# Reading image file as input 
# im = cv2.imread('solid_white.jpg') # reading image file using opencv image object
#im = cv2.imread('black.bmp')        # reading image file using opencv image object
im = cv2.imread('transformed.bmp') # reading image file using opencv image object
# im = cv2.imread('patternB.bmp')
# im = cv2.imread('checkerboard.bmp')
print("Input image")
print(im.dtype)
print(im.shape)
b,g,r = cv2.split(im)  
ret,thresh2 = cv2.threshold(b,254,255,cv2.THRESH_BINARY)
print("Thresholded image")
print(thresh2.dtype)
print(thresh2.shape)
# im_resized = cv2.resize(im, (1280,720), interpolation=cv2.INTER_LINEAR)      # resizing images   

# correcting colors for conversion to PIL object
# b,g,r = cv2.split(im_resized)   
# img = cv2.merge((r,g,b))

# Computing monitor position and size
# for m in get_monitors():
#     print(str(m))
# Haad: Extract monitor (origin) coordinates with res 1280x720 and set them as x,y
# x = (ws/2) - (w/2) + 100
# y = (hs/2) - (h/2) + 100

im = Image.fromarray(thresh2)        # converting image to PIL object

# Shutter control
# board = pyfirmata.Arduino('COM3')
# board.digital[2].write(1)
# board.digital[3].write(1)

app = Test(im,1280,720)
