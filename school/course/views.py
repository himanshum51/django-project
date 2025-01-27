from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def ans(request):
    return HttpResponse('<p>Himanshu course</p>') 