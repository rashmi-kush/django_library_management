from django.shortcuts import render
def showwelcomepage(request):
    return render(request,'mainsite/base.html')
def showbooks(request):
    return render(request,'mainsite/viewbooks.html')

