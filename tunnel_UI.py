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

def camera_choose():
    global camera_num, coordinatefile, pointfile, numberfile, configfile, file_license_num, file_camera_num, image, point_x, point_y, number
    camera_num = str(var8.get())

    # initailize
    number = 0
    point_x = []
    point_y = []
    # name of config file
    coordinatefile = os.path.join(os.getcwd(), "config", "coordinate")
    pointfile = os.path.join(os.getcwd(), "config", "point")
    numberfile = os.path.join(os.getcwd(), "config", "number")

    coordinatefile = coordinatefile + camera_num + ".txt"
    if os.path.exists(coordinatefile):
        os.remove(coordinatefile)
    pointfile = pointfile + camera_num + ".txt"
    if os.path.exists(pointfile):
        os.remove(pointfile)
    numberfile = numberfile + camera_num + ".txt"
    if os.path.exists(numberfile):
        os.remove(numberfile)

    configfile = os.path.join(os.getcwd(), "config", "image1")
    if (var8.get() > 10):
        configfile = os.path.join(os.getcwd(), "config", "image2")
    # load image to configure
    image_list = os.listdir(configfile)
    image_path = ""
    
    for img in image_list:
        if (var8.get() < 10 and img[file_license_num] == "1" and img[file_camera_num] == camera_num):
            image_path= img
        elif (var8.get() == 10 and img[file_license_num] == "1" and img[file_camera_num:file_camera_num + 2] == camera_num):
            image_path = img
        elif (var8.get() > 10 and img[file_license_num] == "1" and img[file_camera_num] == camera_num[1]):
            image_path = img

    # read first image
    image = cv2.imread(os.path.join(configfile, image_path))

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

def save():
    global number, numberfile, point_x, point_y, pointfile
    # save number of point
    f = open(numberfile, "a")
    f.write(str(int(number)) + " ")
    f.close()

    # use y sort point list
    point_y, point_x = zip(*sorted(zip(point_y, point_x)))

    f = open(pointfile, "a")
    for i in range(len(point_x)):
        f.write(str(int(point_x[i] * 3.2)) + "\n")
        f.write(str(int(point_y[i] * 3.2)) + "\n")
    f.close()
    #root.destroy()
    #os.system("./darknet detector test ./cfg/ncsist4.data ./cfg/yolov3-tiny-ncsist4.cfg ./yolov3-tiny-ncsist4_best.weights")

def finish():
    root.destroy()
    os.system("./darknet detector test ./cfg/ncsist4.data ./cfg/yolov3-tiny-ncsist4.cfg ./yolov3-tiny-ncsist4_best.weights")

interval = 5

point_x = []
point_y = []

number = 0
direction = "up"

configfile = ""
file_license_num = 18
file_camera_num = 20
coordinatefile = ""
pointfile = ""
numberfile = ""

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

# choose camera
# speed 
label4 = Label(frame2,text="選擇相機: ", font=('Arial', 12))
label4.pack(pady=5)

camera_num = "1"
var8 = IntVar(value=1)

c1 = Radiobutton(frame2, text='1中仁隧道南下149K+257', variable=var8, value=1,
                    command=camera_choose)
c1.pack()

c3 = Radiobutton(frame2, text="2中仁隧道南下150K+290", variable=var8, value=2,
                    command=camera_choose)
c3.pack()

c5 = Radiobutton(frame2, text='3中仁隧道南下151K+947', variable=var8, value=3,
                    command=camera_choose)
c5.pack()

c7 = Radiobutton(frame2, text="4中仁隧道南下152K+937", variable=var8, value=4,
                    command=camera_choose)
c7.pack()

c9 = Radiobutton(frame2, text='5中仁隧道南下153K+777', variable=var8, value=5,
                    command=camera_choose)
c9.pack()

c11 = Radiobutton(frame2, text="6中仁隧道北上153K+718", variable=var8, value=6,
                    command=camera_choose)
c11.pack()

c13 = Radiobutton(frame2, text='7中仁隧道北上152K+904', variable=var8, value=7,
                    command=camera_choose)
c13.pack()

c14 = Radiobutton(frame2, text="8中仁隧道北上151K+607", variable=var8, value=8,
                    command=camera_choose)
c14.pack()

c15 = Radiobutton(frame2, text="9中仁隧道北上150K+299", variable=var8, value=9,
                    command=camera_choose)
c15.pack()

c16 = Radiobutton(frame2, text="10中仁隧道北上149K+231", variable=var8, value=10,
                    command=camera_choose)
c16.pack()

c2 = Radiobutton(frame2, text="1仁水隧道南下155K+207", variable=var8, value=11,
                    command=camera_choose)
c2.pack()

c4 = Radiobutton(frame2, text="2仁水隧道南下155K+638", variable=var8, value=12,
                    command=camera_choose)
c4.pack()

c6 = Radiobutton(frame2, text="3仁水隧道南下157K+888", variable=var8, value=13,
                    command=camera_choose)
c6.pack()

c8 = Radiobutton(frame2, text="4仁水隧道北上157K+888", variable=var8, value=14,
                    command=camera_choose)
c8.pack()

c10 = Radiobutton(frame2, text="5仁水隧道北上157K+038", variable=var8, value=15,
                    command=camera_choose)
c10.pack()

c12 = Radiobutton(frame2, text="6仁水隧道北上155K+207", variable=var8, value=16,
                    command=camera_choose)
c12.pack()

# interval
interval_number = StringVar()
interval_number.set("5")

label1 = Label(frame2,text="每個參考點的間隔距離: ", font=('Arial', 12))
label1.pack(pady=20)
e1 = Entry(frame2, textvariable = interval_number)
e1.pack(pady=0)

b = Button(frame2,
    text='儲存',
    width=15, height=2, 
    command=save)
b.pack(side="top", pady=20)

b3 = Button(frame2,
    text='完成',
    width=15, height=2, 
    command=finish)
b3.pack(side="top", pady=20)

root.mainloop()
