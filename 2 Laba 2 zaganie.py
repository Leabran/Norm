str2 = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса;_' \
       'Иванов;Семен;' \
       'Игоревич;22 года;Студент 2 курса;'
str2 = str2.split(';_')
for i in range(0, len(str2)-1):
    string = str2[i]
    string = string.split(';')
    print(string[0] + ' ' + string[1] + ' ' + string[2] + '       ' + string[4] + '        ' + string[3])

