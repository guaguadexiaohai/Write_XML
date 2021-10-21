import csv
import os
import re
import json
from nltk.tokenize import word_tokenize
from numpy import random
path = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\yichakan'

file_num = os.listdir(path)
id = 1

def search_entity(sentence):
    e1 = re.findall(r'<e1>(.*)</e1>', sentence)[0]
    e2 = re.findall(r'<e2>(.*)</e2>', sentence)[0]
    sentence = sentence.replace('<e1>' + e1 + '</e1>', ' <e1> ' + e1 + ' </e1> ', 1)
    sentence = sentence.replace('<e2>' + e2 + '</e2>', ' <e2> ' + e2 + ' </e2> ', 1)
    sentence = word_tokenize(sentence)
    sentence = ' '.join(sentence)
    sentence = sentence.replace('< e1 >', '<e1>')
    sentence = sentence.replace('< e2 >', '<e2>')
    sentence = sentence.replace('< /e1 >', '</e1>')
    sentence = sentence.replace('< /e2 >', '</e2>')
    sentence = sentence.split()

    return sentence

def search_entity2(label,sentence):
    e1 = re.findall(r'<e1>(.*)</e1>', sentence)[0]
    e2 = re.findall(r'<e2>(.*)</e2>', sentence)[0]
    sentence = sentence.replace('<e1>' + e1 + '</e1>', ' <e1> ' + e1 + ' </e1> ', 1)
    sentence = sentence.replace('<e2>' + e2 + '</e2>', ' <e2> ' + e2 + ' </e2> ', 1)
    # sentence = word_tokenize(sentence)
    # sentence = ' '.join(sentence)
    sentence = sentence.replace('< e1 >', '<e1>')
    sentence = sentence.replace('< e2 >', '<e2>')
    sentence = sentence.replace('< /e1 >', '</e1>')
    sentence = sentence.replace('< /e2 >', '</e2>')

    n = random.randint(1,6)
    if label == 'cause-effect((e1,e2))':
        cp = e1 + '\t' + e2
    elif label == 'cause-effect((e2,e1))':
        cp = e2 + '\t' + e1
    #sentence = sentence.split()

    # assert '<e1>' in sentence
    # assert '<e2>' in sentence
    # assert '</e1>' in sentence
    # assert '</e2>' in sentence

    return cp


def Pattern(n,e1,e2):
    if n == 1:
        sentence = e1 + " make " + e2 + " take place. "
    elif n == 2:
        sentence = e1 + " cause " + e2 + ". "
    elif n == 3:
        sentence = e1 + " lead to " + e2 + ". "
    elif n == 4:
        sentence = e1 + " is the reason of " + e2 + ". "
    elif n == 5:
        sentence = e1 + " result in " + e2 + ". "
    elif n == 6:
        sentence = e1 + " induce " + e2 + ". "
    return sentence

# label_train = open('./label_sentence/train/label.txt', 'w', encoding='utf-8')
# sentence_train = open('./label_sentence/train/sentence.txt', 'w', encoding='utf-8')
# label_test = open('./label_sentence/test/label.txt', 'w', encoding='utf-8')
# sentence_test = open('./label_sentence/test/sentence.txt', 'w', encoding='utf-8')
# test_id = 21620
# train_id = 1
words_file = './label_sentence/words.txt'
cnt = 0
word_list = []
for num in file_num:
    cnt = 0
    file_path = path + '\\' + num
    with open(file_path,'r',encoding='gbk') as f:
        reader = csv.reader(f)
        for line in reader:
            cnt += 1
            print(cnt)
            print(num)
            content = line[0]
            x = re.sub(r"\\n", "", content)
            x = x.replace('\\n','')
            x = x.replace('\n', '')
            x = x.replace('\r', '')
            y = re.sub(r"\"\"", "", x)
            z = re.sub\
                (r"\"", "", y)
            content = re.sub(r"\\", "", z)
            label = line[1].lower()
            #pattern = '\t<item id="' + str(id) + '" label="' + label + '">\n\t\t<sentence>' + content + '</sentence>\n\t</item>\n'
            words = content.split()
            if len(words) <= 250:
                if label in ['noncause','cause-effect((e1,e2))', 'cause-effect((e2,e1))']:
                    for word in words:
                        if word not in word_list:
                            word_list.append(word)
                        else:
                            continue
                id += 1
    f.close()
    print(id)

fw = open(words_file,'w+',encoding = 'utf-8')
for word in word_list:
    fw.write(word + '\n')

fw.close()

print("Finish!")