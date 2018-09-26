from django.shortcuts import render
from YIDT_app.models import Car
from . import forms
from YIDT_app.forms import UserForm, UserProfileInfoForm

#FOR LOGIN IMPORTS
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

#EXTRA IMPORTS (TEMPORARY)
import os
import random

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('someone tried to login and failed')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html',{})

def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required
def index(request):
    Cars_list = Car.objects.order_by('-Power')
    my_dict = {'Cars': Cars_list}
    return render(request, 'index.html',context =my_dict)

@login_required
def details(request):
    Car_list = Car.objects.order_by('Power')
    car_nr = random.randint(0,len(Car_list)-1)
    currCar = Car_list[car_nr]
    my_dict = {'Make': currCar.Make,
    'Model':currCar.Model,
    'Owner':currCar.Owner,
    'Color':currCar.Color,
    'Year':currCar.Year,
    'Gear':currCar.Gear,
    'Weight':currCar.Weight,
    'Fuel':currCar.Fuel,
    'Power_hp':currCar.Power,
    'HK-Kg':currCar.Power,
    'Plate':currCar.Plate,
    'Img': currCar.Img,}
    return render(request, 'details.html',context =my_dict)

@login_required
def form_name_view(request):
    form = forms.NewCar()
    if request.method == 'POST':
        form = forms.NewCar(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'add_new_car.html', {'form':form})
