# 3
import csv


def search(iid, data):
    for stroka in data:
        if stroka[1] == iid:
            return stroka


with open('rocket.txt',encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter='@'))

    iid = input()
    while iid != 'nlo':
        stroka = search(iid, data)
        if stroka is None:
            print('такой сигнал еще не был получен')
        else:
            print(f'Шифр: {iid} от: {stroka[-1]} был получен {stroka[0]}')
        iid = input()
