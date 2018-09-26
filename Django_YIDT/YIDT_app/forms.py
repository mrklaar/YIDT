from django import forms
from django.core import validators
from YIDT_app.models import Car
from django.contrib.auth.models import User
from YIDT_app.models import UserProfileInfo


class NewCar(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ['Img',]
        #fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
