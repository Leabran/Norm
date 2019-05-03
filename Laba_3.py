import os

file = open("products.txt", "r")
sort = []
for line in file:
	line = line.strip()
	line = line.split(";")
	sort.append(line)

max = int(sort[len(sort)-1][0])


def Work():
	global accessibility
	answer = input('Продолжить? Y/N \n')
	if answer.lower() == 'n':
		accessibility = False


def Find():
	path = input('Введите папку: ')
	count = str(len(next(os.walk(path))))
	print(count)


def Sort():
	global sort
	new_value = sort
	for a in range(0, len(new_value)):
		for b in range(0, len(new_value)-1):
			if int(new_value[a][3]) > int(new_value[a+1][3]):
				line = new_value[a]
				new_value[a] = new_value[a+1]
				new_value[a+1] = line
	return new_value


def Change_stock():
    global max
    new_value = Sort()
    id = []
    print('Введите id товаров, у которых хотите изменить количество по одному.\n'
          'stop - остановка ввода id товаров. \n'
          'Максимальный id = ', max)

    work1 = True
    while work1:
        add = input('ID: ')
        if add.isdigit():
            add = int(add)
            if add <= max:
                id.append(add)
            else:
                print('Максимальный ID = ', max, ', Вы ввели: ', add)
        elif add.lower() == 'stop':
            work1 = False
        else:
            print('Вводите только цифры')


	count = int(input('Введите на сколько хотите уменьшить количество товара,' 
		'если число будет меньше количества, то количество станет равным 0: '))
	for a in range(0, len(new_value)):
		for b in range(0, len(id)):
			if int(new_value[a][0]) == int(id[b]):
				if int(new_value[a][3]) - count >= 0:
					new_value[a][3] = int(new_value[a][3]) - count
				else:
					new_value[a][3] = 0
	return new_value




def Work():
	global accessibility
	answer = input('Продолжить? Y/N \n')
	if answer.lower() == 'n':
		accessibility = False