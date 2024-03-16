import csv

# функция создания логина в формате Фамилия_ИО
def create_login(s, count, nazv):
    login = f'{count}{s}{nazv[0]}'
    return login


with open('rocket.txt', encoding='utf-8') as file, open('rocket_code.csv', 'w', encoding='utf-8',newline='') as new_file:
    data = list(csv.reader(file, delimiter='@'))
    mass = sorted(data[1:])
    res = csv.writer(new_file, delimiter='@')
    data[0].append('queue')
    res.writerow(data[0])
    count = 0
    for stroka in mass:
        count += 1
        stroka.append(create_login(stroka[1],count,stroka[2]))
        res.writerow(stroka)