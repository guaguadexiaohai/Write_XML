import csv
import os

path = 'E:\Code\DATA\data\SemEval-2020-Task5-Dataset\Subtask-2\subtask2_test.csv'

workspace = 'E:/Code/DATA/New_data'

with open(path, 'r',encoding='utf-8', newline='') as file:
    csvreader = csv.reader(file)
    #a = next(csvreader)
    #print(a)
    i = 0
    j = 91
    for row in csvreader:
        #print(row)
        #print(f'i is {i}, j is {j}')
        # 每128个就j加1， 然后就有一个新的文件名
        if i % 1000 == 0:
            j += 1
            #print(f"csv {j} 生成成功")
        # csv_path = os.path.join('../new_csv_file/', 'development (4)/' + str(j) + '.csv')
        csv_path = os.path.join(workspace, '{}.csv'.format(j))
        # print('/'.join(path.split('/')[:-1]))
        #print(csv_path)
        # 不存在此文件的时候，就创建
        if not os.path.exists(os.path.dirname(csv_path)):
            os.makedirs(os.path.dirname(csv_path))
            with open(csv_path, 'w',encoding='utf-8', newline='') as file:
                csvwriter = csv.writer(file)
                # csvwriter.writerow(['image_url'])
                csvwriter.writerow(row)
            i += 1
        # 存在的时候就往里面添加
        else:
            with open(csv_path, 'a',encoding='utf-8', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(row)
            i += 1