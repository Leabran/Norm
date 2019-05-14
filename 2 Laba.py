string1 = "Ли, Литий, Лизергининовый, Лимузин, лицо, литва"
string2 = list(filter(lambda x : x[5:], string1.split()))
print (string2)
