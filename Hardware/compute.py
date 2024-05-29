try:
    import Tkinter as tk
except:
    import tkinter as tk

from PIL import Image, ImageTk, ImageDraw
from matplotlib import image
import numpy as np
from matplotlib import pyplot as plt
import cv2, logging, matplotlib
from screeninfo import get_monitors
from roipoly import MultiRoi
from roipoly import RoiPoly
import os
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
        self.root.destroy()
        
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
        print("Backend: TkAgg")
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
        print("Backend: WXAgg")
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)
        print("Backend: QT/GTK")       


logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s '
                           '%(module)s.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.INFO)

# Reading raw image file
Mask = np.zeros((720,1280),dtype='bool')

# Shutter control OFF
# board = pyfirmata.Arduino('COM3')
# board.digital[2].write(0)
# board.digital[3].write(0)

# Affine tranformation matrix (this needs to be transpose of the MATLAB matrix)
# M = np.array([[1.7057,-0.0647,-1505.6],[-0.0418,-1.0378,1009.3],[0,0,1]],dtype=np.float32)
# M = np.array([[1.2033,0.0622,-77.5409],[0.0570,-1.0861,1164.1],[0,0,1]],dtype=np.float32)
M = np.array([[1.1868,0.0558,75],[0.0620,-1.0783,1100.1],[0,0,1]],dtype=np.float32)

img_black = image.imread('black.bmp')
iter = 0
current_path = os.path.join(os.getcwd(),'mask')
for filename in os.listdir(current_path):
    file_path = os.path.join(current_path, filename)
    if filename.endswith('.cimg'):
        f = open(file_path,'rb')
        # Wasting first two lines
        f.readline().rstrip()
        f.readline().rstrip()
        # Storing data in array and formatting the array
        src = np.fromfile(f, np.float32)
        src = np.rint(src)
        indices_arr = np.nonzero(src)
        indices_arr = np.asarray(indices_arr)
        src = src[indices_arr]
        src = np.reshape(src,(2,int(src.size/2)),order='F')
        src = np.transpose(src)
        print(src)  # printing formatted array
        z_trans = np.ones((len(src),1),dtype=np.float32)
        src = np.hstack((src,z_trans))
        dst = np.empty((len(src),3),dtype=np.float32)
        # Applying Affine transform
        for iter_1 in range(len(src)):
            dst[iter_1,:] = np.matmul(M,np.transpose(src[iter_1,:]))
        # Creating ROI object
        obj = RoiPoly(fig=None, ax=None, color='b',roicolor=None, show_fig=False, close_fig=True)
        list_x = dst[:,0]
        list_y = dst[:,1]
        obj.x = list_x
        obj.y = list_y
        np.add(Mask,obj.get_mask(img_black),out = Mask)
        iter = iter + 1
        print(dst)
        f.close()

im = Image.fromarray(Mask)
im.save("transformed.bmp")
