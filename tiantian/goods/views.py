from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def detail(request):
    return render(request,'detail.html')
