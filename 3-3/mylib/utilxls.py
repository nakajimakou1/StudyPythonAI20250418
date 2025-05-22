# 
import pathlib
from pathlib import Path
import cv2 as cv
import openpyxl
from openpyxl.styles.borders import Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Font, Protection

# sort参考 https://dlrecord.hatenablog.com/entry/2020/07/30/230234
import re
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def replace_spchar(search_filename_path) :

    # 特殊文字回避処理
    chk_file_search_path = search_filename_path.replace("〜","～")
    chk_file_search_path = chk_file_search_path.replace("～","?")
    chk_file_search_path = chk_file_search_path.replace("：","?")

    # https://note.nkmk.me/python-glob-usage/　  # 正規表現回避
    chk_file_search_path = chk_file_search_path.replace("[","?")  # 正規表現回避
    chk_file_search_path = chk_file_search_path.replace("]","?")  # 正規表現回避

    return chk_file_search_path

def makemovie(img_fname, movname):
    ### Movie build
    size = (0,0)
    frame_rate = 20

    # height = 800
    # width = 1280
    height = 400
    width = 640
    size = (width, height)
    # movname = './' + file_name + '.mp4'
    codec = cv.VideoWriter_fourcc('m','p','4','v')
    video = cv.VideoWriter(movname, codec, frame_rate, size)

    for fname in img_fname:
        print(fname)
        img = cv.imread(fname)
        img = cv.resize(img, dsize=(640, 400))
        video.write(img)

    video.release()
    return
