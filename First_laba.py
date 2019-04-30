"""PyCharm_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
