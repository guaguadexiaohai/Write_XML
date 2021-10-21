import csv
import os
import re
import json
from nltk.tokenize import word_tokenize
from numpy import random
path = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\yichakan'

file_num = os.listdir(path)
id = 1

# in_file_train = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\\train.csv'
# in_file_test = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\\test.csv'
# in_file_train = './train_single.csv'
# in_file_test = './test_single.csv'
# in_f_train = open(in_file_train,'w+',encoding='utf-8',newline="")
# writer_train = csv.writer(in_f_train)
# head = ['content','label']
# writer_train.writerow(head)
#
# in_f_test = open(in_file_test,'w+',encoding='utf-8',newline="")
# writer_test = csv.writer(in_f_test)
# writer_test.writerow(head)

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

    # assert '<e1>' in sentence
    # assert '<e2>' in sentence
    # assert '</e1>' in sentence
    # assert '</e2>' in sentence

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
        cp = Pattern(n,e1,e2)
    elif label == 'cause-effect((e2,e1))':
        cp = Pattern(n,e2,e1)
    sentence = sentence + cp
    #sentence = sentence.split()

    # assert '<e1>' in sentence
    # assert '<e2>' in sentence
    # assert '</e1>' in sentence
    # assert '</e2>' in sentence

    return sentence


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

fw_train = open('./CNN_DATA/train.txt', 'w', encoding='utf-8')
fw_test = open('./CNN_DATA/test.txt', 'w', encoding='utf-8')
fw_train_aug = open('./CNN_DATA/train_aug.txt', 'w', encoding='utf-8')
fw_test_aug = open('./CNN_DATA/test_aug.txt', 'w', encoding='utf-8')
test_id = 21620
train_id = 1
cnt = 0
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
                    if id % 5 == 0:
                        if label == 'noncause':
                            sentences1 = words
                            sentences2 = content
                        else:
                            #sentences = get_CP(label, content)
                            #sentences1 = search_entity(content)
                            sentences2 = search_entity2(label,content)
                        fw_test.write('{}\t"{}"'.format(str(test_id),content))
                        fw_test.write('\n')
                        fw_test.write(label + '\n')
                        fw_test.write('\n')

                        fw_test_aug.write('{}\t"{}"'.format(str(test_id), sentences2))
                        fw_test_aug.write('\n')
                        fw_test_aug.write(label + '\n')
                        fw_test_aug.write('\n')

                        test_id += 1
                    else:
                        if label == 'noncause':
                            sentences1 = words
                            sentences2 = content
                        else:
                            #sentences = get_CP(label, content)
                            #sentences1 = search_entity(content)
                            sentences2 = search_entity2(label,content)
                        fw_train.write('{}\t"{}"'.format(str(train_id), content))
                        fw_train.write('\n')
                        fw_train.write(label + '\n')
                        fw_train.write('\n')

                        fw_train_aug.write('{}\t"{}"'.format(str(train_id), sentences2))
                        fw_train_aug.write('\n')
                        fw_train_aug.write(label + '\n')
                        fw_train_aug.write('\n')
                        train_id += 1
                id += 1
    f.close()
    print(id)
fw_test.close()
fw_train.close()
fw_test_aug.close()
fw_train_aug.close()
print(id)