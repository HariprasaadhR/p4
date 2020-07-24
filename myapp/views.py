from django.shortcuts import render
from django.http import HttpResponse
#from math import factorial
# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome to views of an app</h1>')

def home(request):
    return render(request,'myapp/home.html',{'name':'Hariprasaadh'})

def fact(request,n):
    n=int(n)
    while(n>0):
        facts=n*(n-1)
        n-=1
    return HttpResponse('<h4>factorial is {}<h4>'.format(facts))