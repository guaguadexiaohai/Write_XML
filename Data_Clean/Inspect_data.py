import os
import csv
import re
import pandas as pd

#去除空白行
def remove_black():
    file_old = open('../Data/depression22.txt', 'r', encoding='utf-8-sig')
    file_new = open('../Data/new.txt', 'w', encoding='utf-8-sig')

    for text in file_old.readlines():
        if text.split():
            file_new.write(text.lower())
#remove_black()

#去掉长度小于30的字符串
def remove_short():
    file_old = open('../Data/new.txt', 'r', encoding='utf-8-sig')
    file_new = open('../Data/long.txt', 'w', encoding='utf-8-sig')

    for text in file_old.readlines():
        if len(text) >= 30:
            file_new.write(text)

#remove_short()


#移除非法字符
def remove_illegal():
    file_old = open('../Data/new.txt', 'r', encoding='utf-8-sig')
    file_new = open('neg1.txt', 'w', encoding='utf-8-sig')

    for text in file_old.readlines():
        text = str(bytes(text, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
        file_new.write(text)
#remove_illegal()

def clean_str(text):
    text = text.lower()
    # Clean the text
    text = re.sub(r"\\n","",text)
    text = re.sub(r"i’m", "i am", text)
    text = re.sub(r"im", "i am", text)
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=$#]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"that's", "that is ", text)
    text = re.sub(r"there's", "there is ", text)
    text = re.sub(r"it's", "it is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"i\'ve", "i have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    #text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    #text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)  # ?
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)  # ?

    return text.strip()

#t = 0
def move_to_csv(t):
    fh = open(r'../Data/data1.csv',"w+",newline='',encoding='utf-8-sig')
    writer = csv.writer(fh)
    writer.writerow(['num','content'])
    data = open(r'../Data/long2.txt','r',encoding='utf-8-sig')
    res = []
    #t = 0
    for text in data.readlines():
        text = clean_str(text)
        content = [t,text]
        writer.writerow(content)
        t += 1
    data.close()
    fh.close()
    return t

#move_to_csv()

def csv_to_csv(t):
    file_out = open('../Data/depression.csv','r',encoding='utf-8-sig')
    reader = csv.reader(file_out)
    file_in = open('../Data/data1.csv','a',encoding='utf-8-sig')
    writer = csv.writer(file_in)

    for row in reader:
        text = row[2]
        text = str(bytes(text, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
        text = clean_str(text)
        content = [t,text]
        t += 1
        writer.writerow(content)
    #file_in = open('../data.csv','w+')

# m = move_to_csv(t)
#
# csv_to_csv(m)

def csv_to_txt():
    file_out = open('E:/Code/DATA/data/ptsd.csv','r',encoding='gbk')
    reader = csv.reader(file_out)
    file_in = open('E:/Code/DATA/data/ptsd.txt','w+',encoding='utf-8-sig')

    for text in reader:
        text = text[0]
        text = str(bytes(text, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
        #text = clean_str(text)
        #text = text.strip(',')
        file_in.write(text + '\n')

    file_in.close()
    file_out.close()

csv_to_txt()