from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hospital.forms import UserForm, babyDetailsForm
import hashlib
# Create your views here.
class home(TemplateView):
    template_name = "hospital/index.html"

def LoginPage(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('hospital:submitform'))

            else:

                return HttpResponse('Something is wrong!')
        else:

            return HttpResponse('Incorrect details')
    else:

        return render(request, 'hospital/login.html')

hashed = ""
def submit_details(request):
    registered = False

    if request.method == "POST":
        user_details = babyDetailsForm(data = request.POST)

        if user_details.is_valid():
            to_hash = str(user_details).encode()
            hashed = hashlib.sha256(to_hash).hexdigest()
            # print(hashed)
            # print(str(user_details))
            #saving user_details now
            user_details.save()

            registered = True

    else:
        user_details = babyDetailsForm()

    return render(request, 'hospital/submitform.html',{'registered': registered , 'user_details' : user_details})
print(hashed)
def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('hospital:login'))
