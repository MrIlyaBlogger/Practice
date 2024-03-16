import csv
with open('rocket.txt',encoding='utf-8') as file, open('rocket_part.txt','w',encoding='utf-8',newline='') as new_file:
    data = list(csv.reader(file,delimiter='@'))
    res = csv.writer(new_file,delimiter='@')
    stroka = []
    stroka.append('rocketPart')
    stroka.append('countCode')
    res.writerow(stroka)
    list = []
    for stroka in data[1:]:
        count = 0
        part = stroka[-1]
        if part not in list:
            list.append(part)
            dob = []
            for row in data[1:]:
                if row[-1] == part:
                    count += 1
            dob.append(part)
            dob.append(count)
            res.writerow(dob)

with open('rocket_part.txt',encoding='utf-8') as prog:
    mass = csv.reader(prog,delimiter='@')
    nazv = input()
    for stroka in mass:
        if stroka[0] == nazv:
            print(stroka[-1])