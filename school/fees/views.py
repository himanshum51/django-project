# views.py
from django.shortcuts import render

# Create your views here.
def ans(request):
    return render(request, 'fees/stu1.html')

def ans2(request):
    return render(request, 'fees/stu2.html')

def ans3(request):
    return render(request, 'fees/base.html')
