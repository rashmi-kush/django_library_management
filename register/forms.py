from django import forms
from register import models
class Regform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta:
       model=models.registermod
       fields = ("__all__")
       labels ={'userid':'Enter userid',
       'password':'Enter password'}
       error_messages={'userid':{'required':'Id required!','unique':'Id already exists!!'},
       'password':{'required':'Password required!'}}
       widgets={'userid':forms.Textarea(attrs={"placeholder":"Type your email_id"}),
       'password':forms.PasswordInput(attrs={"placeholder":"Type your password"}),}

              
               