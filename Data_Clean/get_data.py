import csv
import pandas as pd
import re
import codecs
def remove_stopwords(text):
    word_list = text.split()
    stopword = loan_stopwords()
    words = []
    for word in word_list:
        if word not in stopword and word != ' ':
            #print('1')
            words.append(word)
    return words

def loan_stopwords():
    stopwords = []
    with codecs.open('../Data/stopwords.txt', 'r', 'utf-8') as f:
        for each in f.readlines():
            each = each.strip('\n')
            each = each.strip('\r')
            each = each.strip()
            stopwords.append(each)
    return stopwords

def move_txt():
    f = open('../Data/data.csv', 'r', encoding='utf-8')
    txt = open('../Data/used_for_depend.txt', 'w+', encoding='utf-8')
    reader = csv.reader(f)
    for row in reader:
        text = row[1]
        if text != 'content':
            txt.write(text)
            txt.write('\n')
        #text = remove_stopwords(text)
        # for word in text:
        #     txt.write(word)
        #     txt.write(' ')


    f.close()
    txt.close()

move_txt()
