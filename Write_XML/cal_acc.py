import json

path_data_file_json = 'test.json'
labels_org = []
labels_predicted = []
with open(path_data_file_json, 'r', encoding='utf-8') as fr:
    for line in fr:
        line = json.loads(line.strip())
        #print(line['sentence'])
        label1 = line['relation']
        labels_org.append(label1)
fr.close()

path_data_file_pre = 'predicted_result.txt'
with open(path_data_file_pre, 'r', encoding='utf-8') as ft:
    lines = ft.readlines()
    for line in lines:
        #print(line)
        label2 = line[5:]
        #print(label2.lstrip('\t'))
        label2 = label2.lstrip('\t')
        labels_predicted.append(label2.strip('\n'))
ft.close()

print("length of orginal is %d" % len(labels_org))
print("length of predicted is %d" % len(labels_predicted))

log = open('logs_aug.txt', 'w', encoding='utf-8')
log.write('Number \t\t labels_org \t\t labels_predicted\n')
cnt = 0

if len(labels_org) == len(labels_predicted):
    for i in range(len(labels_org)):
        if labels_org[i] == labels_predicted[i]:
            cnt += 1
        else:
            log.write(str(i) + '\t\t' + labels_org[i] + '\t\t' + labels_predicted[i] + '\n')
log.close()

acc = cnt / len(labels_predicted)

print('{%.4f}' % acc)



