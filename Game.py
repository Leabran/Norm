

import random

NumbersR = random.randint(1,100)
NumbersU = 0
while NumbersU != NumbersR:

    NumbersU = int(input("Введите число от 1 до 100"))

    if NumbersU > NumbersR:
        print("Число должно быть меньше")
    elif NumbersU < NumbersR:
        print("Число должно быть больше")
    else:
        print("Вы угадли число!")
