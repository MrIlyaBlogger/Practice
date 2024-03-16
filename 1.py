import csv
with open('rocket.txt',encoding='utf-8') as file, open('rocket_part.txt','w',encoding='utf-8',newline='') as new_file:
    data = list(csv.reader(file,delimiter='@'))
    res = csv.writer(new_file,delimiter='@')
    print(res)
    for stroka in data[1:]:
        part = stroka[-1]
