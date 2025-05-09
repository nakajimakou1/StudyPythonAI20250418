# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv # https://reffect.co.jp/python/python-csv-manuplulate

x_data = np.arange(1,100) # x軸のメモリ用
#print(x_data)

# ※np.loadtxtでは、ヘッダに文字があるとエラーとなってしまう。
# rows = np.loadtxt("test2-1.csv", delimiter = ",")

file_path = './test2-1.csv'
fp = open(file_path,'r',encoding="shift-jis") #CSVファイルをオープン utf-8 cp932 shift-jis
rows = csv.reader(fp, delimiter=',')
header = next(rows) #header行をスキップ
print(header)

for row in rows:
    print(row)

    #x = rows[:, 0]
    plt.figure(figsize=(16,10), dpi=80)
    plt.plot(x_data[0:6], row) # 折れ線グラフ

    plt.title("データグラフ", fontsize=22, fontname="MS Gothic" )
    plt.xlabel('# Xvalue')
    plt.ylabel('# Yvalue')

    # 棒グラフを表示
    plt.show()
