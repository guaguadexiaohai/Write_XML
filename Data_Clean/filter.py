# 情感词典过滤
import csv
import re
import os

emotion_path = 'E:\Code\Python\Project\Causality_Extraction\Data\Emotion list2.txt'
#data_path = 'E:\Code\DATA\data\depression.txt'
data_path = 'E:/Code/DATA/data/ptsd.txt'
new_data_path = 'E:/Code/DATA/data/after filter ptsd.txt'

def load_emotion_list():
    emotion_list = []
    with open(emotion_path,'r',encoding='utf-8-sig') as f:
        lines = f.readlines()
        for line in lines:
            text = str(line)
            emotion_list.append(text)
    return emotion_list

def filter(emotion_list):
    with open(new_data_path,'a',encoding='utf-8-sig') as file_in:
        with open(data_path, 'r',encoding='utf-8-sig') as file:
            line = file.readline()
            while line:
                #line = line.lower()
                words = line.split()
                if len(words) < 200:
                    for word in words:
                        word = word + '\n'
                        if word in emotion_list:
                            file_in.write(line + '\n')
                            break
                        else:
                            continue
                else:
                    continue
                line = file.readline()
        file.close()
    file_in.close()



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
    #text = re.sub(r"\0s", "0", text)  # ?
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)  # ?

    return text.strip()



#print(emotion_list)
#filter(emotion_list)
def filter2(emotion_lst):
    file_out = open(data_path,mode = 'r',encoding='utf-8')
    reader = file_out.readlines()
    file_in = open(new_data_path,mode='w+',encoding='utf-8')
    for line in reader:
        #line = line[3]
        line = str(line)
        #line = line.lower()
        #line = clean_str(line)
        words = line.split()
        if len(words) < 200:
            for word in words:
                word = word + '\n'
                if word in emotion_list:
                    file_in.write(line)
                    break
                else:
                    continue
        else:
            continue
    file_in.close()
    file_out.close()

emotion_list = load_emotion_list()
filter2(emotion_list)