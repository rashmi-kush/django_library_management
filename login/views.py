from django.shortcuts import render
from register import models
from login import forms

def loginview(request):
    context={}
    if request=='POST':
      loginobj=forms.Loginform(request.POST)
      if loginobj.is_valid():
          uid=loginobj.cleaned_data['username']
          pwd=loginobj.cleaned_data['password']
          modobj=loginobj.save(commit=False)
          dbdata=models.registermod.objects.filter(userid=uid,password=pwd)
          if len(dbdata)==0:
            context['failed']='failed'
            loginobj=forms.Loginform()
          else:
            username=dbdata[0].username
            request.session['logedin']=True
            return render(request,'login/seceretpage.html',{'username':username})
    else:
       loginobj=forms.Loginform()
    context['logform']=loginobj
    return render(request,'login/signin.html',context) 


def logoutview(request):
  try:
    del request.session['login']
  except KeyError:
    context={}
    loginobj=forms.Loginform()
    context['logform']=loginobj
    return render(request,'login/signin.html',context) 

  return render(request,'login/logout.html')

def operation(request):
  return render(request,'login/operation.html')

