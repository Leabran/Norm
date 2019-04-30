
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третье число"))
k = int(input("Введите четвёртое число"))

rez = ((a ** 2 / b ** 2) + (c ** 2 * a ** 2)) / (a + b + (c * (k - (a / b ** 3))) + c + ((k / b) - (k / a)))
if b == 0 or a == 0:
    print("На ноль делить нельзя!")
elif b != 0 and a != 0:
    print(rez)
