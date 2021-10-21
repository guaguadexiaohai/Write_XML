import csv
import os
import re

path = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\yichakan'

file_num = os.listdir(path)
id = 1
# in_file_train = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\\train.csv'
# in_file_test = 'E:\Code\Python\Project\Causality_Extraction\Write_XML\\test.csv'
in_file_train = './train_single.csv'
in_file_test = './test_single.csv'
in_f_train = open(in_file_train,'w+',encoding='utf-8',newline="")
writer_train = csv.writer(in_f_train)
head = ['content','label']
writer_train.writerow(head)

in_f_test = open(in_file_test,'w+',encoding='utf-8',newline="")
writer_test = csv.writer(in_f_test)
writer_test.writerow(head)

for num in file_num:
    print(num)
    file_path = path + '\\' + num
    with open(file_path,'r',encoding='gbk') as f:
        reader = csv.reader(f)
        for line in reader:
            content = line[0]
            x = re.sub(r"\\n", "", content)
            x = re.sub(r"\"\"", "", x)
            content = re.sub(r"\\", "", x)
            content = str(bytes(content, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
            label = line[1].lower()
            #pattern = '\t<item id="' + str(id) + '" label="' + label + '">\n\t\t<sentence>' + content + '</sentence>\n\t</item>\n'
            words = content.split()
            if len(words) <= 250:
                if label in ['noncause', 'cause-effect((e1,e2))', 'cause-effect((e2,e1))']:
                    data = [content, label]
                    if id % 5 == 0:
                        writer_test.writerow(data)
                    else:
                        writer_train.writerow(data)
                    id += 1
    f.close()
    print(id)
in_f_test.close()
in_f_train.close()
print(id)