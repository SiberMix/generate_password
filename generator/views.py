import random

from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'generator/home.html',)
def password(request):
    thepassword = ''
    character = list('abcdefghijklmnopqrstuvwxyz')
    len = int(request.GET.get('len'))
    for item in range(len):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password': thepassword})