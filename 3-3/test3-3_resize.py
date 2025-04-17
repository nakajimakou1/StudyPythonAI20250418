# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import csv # https://reffect.co.jp/python/python-csv-manuplulate
import pathlib
import cv2 as cv

def makemovie(img_fname):
    ### Movie build
    size = (0,0)
    frame_rate = 20

    #height = 800
    #width = 1280
    height = 400
    width = 640
    size = (width, height)
    # movname = './' + file_name + '.mp4'
    codec = cv.VideoWriter_fourcc('m','p','4','v')
    video = cv.VideoWriter('temp.mp4', codec, frame_rate, size)

    for fname in img_fname:
        print(fname)
        img = cv.imread(fname)
        img = cv.resize(img, dsize=(640, 400))
        video.write(img)

    video.release()
    
x_data = np.arange(1,10) # x軸のメモリ用
# print(x_data)

# ※np.loadtxtでは、ヘッダに文字があるとエラーとなってしまう。
# df_raw = np.loadtxt("test3-2.csv", delimiter = ",")

file_path = './test3-3.csv'
fp = open(file_path,'r',encoding="shift-jis") #CSVファイルをオープン utf-8 cp932 shift-jis
rows = csv.reader(fp)
header = next(rows) #header行をスキップ

img_fname = []
#print(rows[1])
for ylist_data in rows:  
    # print (ylist_data)

    plt.figure(figsize=(16,10), dpi=80)
    # plt.plot(x_data[0:5], ylist_data[1:6])
    
    # 読み出したCSVデータを数値型に変換して
    ylist = []
    for ylist_dt in ylist_data:
        # print(ylist_dt)
        ylist.append(int(ylist_dt))
    
    plt.bar(x_data[0:5], ylist[1:6], color=cm.Set1.colors[2], width=0.2, label="data/value")

    plt.title("データグラフ", fontsize=22, fontname="MS Gothic" )
    plt.xlabel('# Xvalue')
    plt.ylabel('# Yvalue')
    # plt.xlim(0, 6)
    plt.ylim(1, 50001) # 50000 -> 50001 Max目盛りに「50000」を表示したいため
    plt.xticks(np.arange(0, 6, step=1)) 
    plt.yscale('linear')    # linear     log
    plt.yticks(np.arange(0, 50001, step=10000)) # 50000 -> 50001 Max目盛りに「50000」を表示したいため

    dbgdisp = False # True # False
    if dbgdisp :
        plt.show()
    else:
        # plt.show()
        savefname = "./img/img" + ylist_data[0] + ".png"
        # print("save File name:" + savefname + "\n")
        plt.savefig(savefname)
        img_fname.append(savefname)

fp.close()
makemovie(img_fname)
print("end")