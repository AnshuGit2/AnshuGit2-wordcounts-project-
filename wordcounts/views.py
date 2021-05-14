from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'home.html',{'hithere':'This is me'})

def eggs(request):
    return HttpResponse('<h1>Eggs</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist)})



