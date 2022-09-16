from django import forms
from register import models
class Loginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta:
       modelobj=models.registermod()
       fields = ("userid","password")
       labels ={'userid':'Enter userid',
       'password':'Enter password'}
       error_messages={'userid':{'required':'Id required!'},
       'password':{'required':'Password required!'}}
       widgets={'userid':forms.Textarea(attrs={"placeholder":"Type your email_id"}),
       'password':forms.PasswordInput(attrs={"placeholder":"Type your password"})
       }
