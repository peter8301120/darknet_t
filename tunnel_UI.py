import argparse
import os
import numpy as np
import struct
import cv2
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
import tkinter.simpledialog
from tkinter.font import nametofont
from PIL import Image, ImageTk
import PIL
from tqdm import tqdm
import time

# Determine the origin by clicking
def getorigin(eventorigin):
    global x0,y0, image
    x0 = eventorigin.x
    y0 = eventorigin.y
    r = 3
    image = cv2.circle(image, (x0, y0), r, (255,0,0), 3)
    img = PIL.Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    L.img = img
    L.config(image=L.img)
    root.update()
    #L.create_oval(x0-r, y0-r, x0+r, y0+r, fill = "red")
    L.bind("<Button 1>",getorigin1)

# Determine the origin by clicking
def getorigin1(eventorigin):
    global x1,y1, image, coordinatefile
    x1 = eventorigin.x
    y1 = eventorigin.y
    r = 3
    image = cv2.circle(image, (x1, y1), r, (255,0,0), 3)
    image = cv2.line(image, (x0, y0), (x1, y1), (255,0,0), 3)
    img = PIL.Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    L.img = img
    L.config(image=L.img)
    root.update()

    # save line coordinate
    f = open(coordinatefile, "w")
    f.write(str(int(x0 * 3.2)) + "\n" + str(int(y0 * 3.2)) + "\n")
    f.write(str(int(x1 * 3.2)) + "\n" + str(int(y1 * 3.2)) + "\n")
    f.close()

    tkinter.messagebox.showinfo("Instructions", "請點出欲偵測車道右邊的車道線起始位置", parent=root)
    L.bind("<Button 1>",getorigin2)

# Determine the origin by clicking
def getorigin2(eventorigin):
    global x2,y2, image
    x2 = eventorigin.x
    y2 = eventorigin.y
    r = 3
    image = cv2.circle(image, (x2, y2), r, (255,0,0), 3)
    img = PIL.Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    L.img = img
    L.config(image=L.img)
    root.update()
    #L.create_oval(x0-r, y0-r, x0+r, y0+r, fill = "red")
    L.bind("<Button 1>",getorigin3)

# Determine the origin by clicking
def getorigin3(eventorigin):
    global x3,y3, image, coordinatefile, interval
    x3 = eventorigin.x
    y3 = eventorigin.y
    r = 3
    image = cv2.circle(image, (x3, y3), r, (255,0,0), 3)
    image = cv2.line(image, (x2, y2), (x3, y3), (255,0,0), 3)
    img = PIL.Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    L.img = img
    L.config(image=L.img)
    root.update()

    interval = int(float(interval_number.get()))
    # save line coordinate
    f = open(coordinatefile, "a")
    f.write(str(int(x2 * 3.2)) + "\n" + str(int(y2 * 3.2)) + "\n")
    f.write(str(int(x3 * 3.2)) + "\n" + str(int(y3 * 3.2)) + "\n")
    f.write(str(interval) + "\n")
    f.close()

    tkinter.messagebox.showinfo("Instructions", "請點出參考點位置", parent=root)
    L.bind("<Button 1>",getorigin4)
# Determine the origin by clicking
def getorigin4(eventorigin):
    global x4,y4, image, number, point_x, point_y
    x4 = eventorigin.x
    y4 = eventorigin.y
    r = 3
    image = cv2.circle(image, (x4, y4), r, (0,255,0), 3)
    img = PIL.Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    L.img = img
    L.config(image=L.img)
    root.update()

    point_x.append(x4)
    point_y.append(y4)

    number = number + 1

def str2tuple(s_tuple):
    x = int(s_tuple.split(',')[0][1:])
    y = int(s_tuple.split(',')[1][1:-2])
    return (x,y)

def str2temp(temp_str):
    temp_temp = []
    if len(temp_str) < 5:
        return temp_temp

    l_cnt = 0
    cnt = 0
    x = 0
    y = 0
    frame = 0
    cls = 0
    count = 0
    l_str = len(temp_str.split(","))
    for num in temp_str.split(","):
        if (cnt == 0):
            x = float(num[2:])
            cnt = cnt + 1
            l_cnt = l_cnt + 1
        elif (cnt == 1):
            y = float(num[1:])
            cnt = cnt + 1
            l_cnt = l_cnt + 1
        elif (cnt == 2):
            frame = float(num[1:])
            cnt = cnt + 1
            l_cnt = l_cnt + 1
        elif (cnt == 3):
            cls = float(num[1:])
            cnt = cnt + 1
            l_cnt = l_cnt + 1
        elif (cnt == 4):
            if (l_cnt == l_str - 1):
                count = float(num[1:-2])
            else:
                count = float(num[1:-1])
            temp_temp.append((x, y, frame, cls, count))
            cnt = 0
            l_cnt = l_cnt + 1
    return temp_temp

def openfile():
    global File, l_coordinate, image
    # if load the line coordinate from file
    if (l_coordinate == 1):
       File = askdirectory(parent=root, initialdir="./",title='Select an dictionary')
       l_coordinate = 0
    else:
        File = askdirectory(parent=root, initialdir="./",title='Select an dictionary')
        image_list = os.listdir(File)
        image = image_list[0]


        # read first image
        image = cv2.imread(os.path.join(File, image))

        frame_h = image.shape[0]
        frame_w = image.shape[1]
        wrap_w = int(frame_w / 3.2)
        wrap_h = int(frame_h / 3.2)

        image = cv2.resize(image,(wrap_w, wrap_h),interpolation=cv2.INTER_CUBIC)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original = PIL.Image.fromarray(image)
        img = ImageTk.PhotoImage(original)
        L.img = img
        L.config(image=L.img)
        root.update()

        # make point of lines
        tkinter.messagebox.showinfo("Instructions", "請點出欲偵測車道左邊的車道線起始位置", parent=root)
        L.bind("<Button 1>",getorigin)

def finish():
    global number, numberfile, File, Filepath, point_x, point_y, pointfile
    # save number of point
    f = open(numberfile, "a")
    f.write(str(int(number)) + " ")
    f.close()
    f = open(Filepath, "a")
    f.write(str((File)))
    f.close()

    # use y sort point list
    point_y, point_x = zip(*sorted(zip(point_y, point_x)))

    f = open(pointfile, "a")
    for i in range(len(point_x)):
        f.write(str(int(point_x[i] * 3.2)) + "\n")
        f.write(str(int(point_y[i] * 3.2)) + "\n")
    f.close()
    root.destroy()
    os.system("./darknet detector test ./cfg/ncsist4.data ./cfg/yolov3-tiny-ncsist4.cfg ./yolov3-tiny-ncsist4_best.weights")

interval = 5

point_x = []
point_y = []

number = 0
direction = "up"
# file opened by program
File = ""

coordinatefile = os.path.join(os.getcwd(), "coordinate.txt")
if os.path.exists(coordinatefile):
    os.remove(coordinatefile)
pointfile = os.path.join(os.getcwd(), "point.txt")
if os.path.exists(pointfile):
    os.remove(pointfile)
Filepath = os.path.join(os.getcwd(), "File.txt")
if os.path.exists(Filepath):
    os.remove(Filepath)
numberfile = os.path.join(os.getcwd(), "number.txt")
if os.path.exists(numberfile):
    os.remove(numberfile)

l_coordinate = 0

root = Tk()
root.title("car counting")
root.geometry('1500x800+200+100')
frame_w = 1280
frame_h = 675

# auto save log file
nametofont("TkHeadingFont").configure(size=10)

#setting up a tkinter canvas
L = Label(root, bg = 'white', width = frame_w, height = frame_h)
#L = Canvas(root, width = frame_w, height = frame_h)
L.pack(side="bottom",padx=10, pady=30,anchor=NW)  # NW SE

frame2 = Frame(root)

frame2.place(x=1300, y=30, width = 200, height=800)

# button  開啟檔案
b = Button(frame2,
    text='開啟檔案',
    width=15, height=2, 
    command=openfile)
b.pack(side="top", padx=0, pady=30)

# interval
interval_number = StringVar()
interval_number.set("5")

label1 = Label(frame2,text="每個參考點的間隔距離: ", font=('Arial', 12))
label1.pack()
e1 = Entry(frame2, textvariable = interval_number)
e1.pack(pady=0)

b = Button(frame2,
    text='確定',
    width=15, height=2, 
    command=finish)
b.pack(side="top", pady=30)

root.mainloop()
