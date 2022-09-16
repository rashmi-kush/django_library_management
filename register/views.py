
from django.shortcuts import render
from register import forms
from register import models
def regview(request):
    context={}
    if request.method=='POST':
         regobj=forms.Regform(request.POST)
         if regobj.is_valid():
            userobj=regobj.save()
            regobj=forms.Regform()
            context['done']=True               
    else:
      regform=forms.Regform()
      context['regobj']=regform
    return render(request,'registration/signup.html',context)
