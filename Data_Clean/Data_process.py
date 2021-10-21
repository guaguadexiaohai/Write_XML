# -*- coding=utf-8 -*-

import csv
import pandas as pd
import os
import re
import emoji

path = 'E:\Code\DATA\data\depression2.csv'
path2 = 'E:/Code/DATA/New_data'
path1 = 'E:\Code\DATA\data\depression.csv'
path3 = 'E:/Code/DATA/data/after filter ptsd.txt'

def move():
    with open(path3, 'r', encoding='utf-8-sig') as file1:
        i = 1
        j = 32
        line = file1.readline()
        while line:
            text = line
            text = str(bytes(text, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
            #print(f'i is {i}, j is {j}')
            # 没1000个就j加1， 然后就有一个新的文件名
            if i % 1000 == 0:
                j += 1
                if j >= 41:
                    break
                #print(f"csv {j} 生成成功")
            csv_path = path2 + '/' + str(j) + '.csv'
            # print('/'.join(path.split('/')[:-1]))
            #print(csv_path)
            # 不存在此文件的时候，就创建
            if not os.path.exists(csv_path):
                with open(csv_path, 'w+', newline='') as file:
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(['content'])
                    content = [text]
                    csvwriter.writerow(content)
            # 存在的时候就往里面添加
            else:
                with open(csv_path, 'a', newline='') as file:
                    csvwriter = csv.writer(file)
                    content = [text]
                    csvwriter.writerow(content)
            i += 1
            line = file1.readline()

move()
#remove_long()




