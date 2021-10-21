
"""
情感词典构建
"""
import os
import re
def create_emotion():
    path = '../Data/raw emotion list.txt'
    path2 = '../Data/emotion list2.txt'
    content = []
    with open(path, 'r') as filein:
        lines = filein.readlines()
        for line in lines:
            words = line.split('~')
            for word in words:
                content.append(word)
    filein.close()

    with open(path2, 'a') as fileout:
        for word in content:
            word = word.lower().strip()
            fileout.write(word + '\n')
    fileout.close()

def clean():
    path = 'E:/Code/DATA/data/data.txt'
    path2 = 'E:/Code/DATA/data/data_new.txt'
    file = open(path,mode = 'r', encoding='utf-8')
    file2 = open(path2,mode = 'w+', encoding='utf-8')
    line = file.readline()
    while line:
        line.rstrip("''")
        file2.write(line)
        line = file.readline()
    file.close()
    file2.close()
clean()