import numpy as np
import cv2
import os
from scipy import stats
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import datetime
import time
# center
color = ["red", "yellow", "blue", "black", "white", "gray"]
cluster_color = [[255, 0, 0], [255, 255, 0], [0, 0, 255], [0, 0, 0], [255, 255, 255], [127, 127, 127]]
cluster_color = [[110, 22, 26], [176, 156, 33], [0, 0, 255], [25, 25, 25], [200, 200, 200], [100, 125, 135]]
if not os.path.exists("ftp-upload01_temp"):
    os.mkdir("ftp-upload01_temp")
if not os.path.exists("ftp-upload02_temp"):
    os.mkdir("ftp-upload02_temp")

image_files = os.listdir("./ftp-download01")

for img in image_files:
    if img.endswith(".JPG") and img[18] == '0':
        img_path = os.path.join("./ftp-download01", img)
        image = cv2.imread(img_path)
        image_roi = image[20:60, 5:15 ]
        mean_color = image_roi.mean(axis = 0).mean(axis = 0)
        # BGR to RGB
        RGB_color = [mean_color[2], mean_color[1], mean_color[0]]
        label=vq([RGB_color], cluster_color)[0]
        # save log file and remove picture
        ftp_upload1 = os.path.join(os.getcwd(), "ftp-upload01_temp", img[:10], img[:10] + "_color.txt")
        if not os.path.exists( os.path.join(os.getcwd(), "ftp-upload01_temp", img[:10])):
            os.mkdir( os.path.join(os.getcwd(), "ftp-upload01_temp", img[:10]))
        f = open(ftp_upload1, "a")
        f.write(img[:-4] + "_" + str(label[0]) + "\n")
        f.close()
        os.remove(img_path)

image_files2 = os.listdir("./ftp-download02")

for img in image_files2:
    if img.endswith(".JPG") and img[18] == '0':
        img_path = os.path.join("./ftp-download02", img)
        image = cv2.imread(img_path)
        image_roi = image[20:60, 5:15 ]
        mean_color = image_roi.mean(axis = 0).mean(axis = 0)
        # BGR to RGB
        RGB_color = [mean_color[2], mean_color[1], mean_color[0]]
        label=vq([RGB_color], cluster_color)[0]
        # save log file and remove picture
        ftp_upload2 = os.path.join(os.getcwd(), "ftp-upload02_temp", img[:10], img[:10] + "_color.txt")
        if not os.path.exists( os.path.join(os.getcwd(), "ftp-upload02_temp", img[:10])):
            os.mkdir( os.path.join(os.getcwd(), "ftp-upload02_temp", img[:10]))
        f = open(ftp_upload2, "a")
        f.write(img[:-4] + "_" + str(label[0]) + "\n")
        f.close()
        os.remove(img_path)

# rename
if if not os.path.exists( os.path.join(os.getcwd(), "ftp-upload01")):
            os.rename( os.path.join(os.getcwd(), "ftp-upload01_temp"), os.path.join(os.getcwd(), "ftp-upload01"))
if if not os.path.exists( os.path.join(os.getcwd(), "ftp-upload02")):
            os.rename( os.path.join(os.getcwd(), "ftp-upload02_temp"), os.path.join(os.getcwd(), "ftp-upload02"))
