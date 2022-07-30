from django.shortcuts import render
import random


def index(request):
    return render(request, 'generator/index.html')


def generated(request):
    listok = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('lenght') == 'random':
        lenght = int(random.randint(1, 40))
    else:
        lenght = int(request.GET.get('lenght'))
    if request.GET.get('upper_case') == 'on':
        listok.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('spec_symbols') == 'on':
        listok.extend(list('!@#$%^&*()}{":?><'))
    if request.GET.get('numbers') == 'on':
        listok.extend(list('0123456789'))
    password = ''
    for i in range(lenght):
        password += random.choice(listok)
    return render(request, 'generator/genpass.html', {'password':password})


def aboutme(request):
    return render(request, 'generator/aboutme.html')

