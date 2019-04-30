n = int(input('Введите длину списка: '))
list = []
count = 0
for i in range(0, n):
    list.append(int(input('Введите ' + str(i) + ' элемент списка: ')))
print(list)
list.remove(int(input('Введите  элемент списка: ')))
list.remove(int(input('Введите  элемент списка: ')))
list.insert(0,int(input('Введите новый элемент списка: ')))
list.insert(1,int(input('Введите новый элемент списка: ')))
print(list)






