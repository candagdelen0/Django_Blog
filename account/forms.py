from django import forms
from  django.contrib.auth.forms import PasswordChangeForm
from django.forms import widgets
from django.contrib.auth.models import User

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
