from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {'name':'Akul Gupta'}
    return render(request, 'reservation/home.html',context)
#    return HttpResponse('Hello World')

def studentdetails(request):
    return render(request, 'reservation/studentdetails.html')
    
def bookdetails(request):
    return render(request, 'reservation/bookdetails.html')
    