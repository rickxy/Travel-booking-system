from django import forms
from django import contrib
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import CreateUserForm

def registerPage(request):
        form= CreateUserForm( )  

        if request.method =='POST':
                form = CreateUserForm(request.POST )
                if form.is_valid():
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.success(request, 'Account was created for' + user)
                        return redirect(loginPage)
        context ={'form':form}
        return render(request, "register.html", context)
def loginPage(request):
        if request.method == 'POST' :
               username= request.POST.get('username')
               password=request.POST.get('password')

               user= authenticate(request, username=username, password=password)
               if user is not None:
                       login(request, user)
                       return redirect('home')
        context ={}
        return render(request, "login.html", context)
        
def index(request):
        context ={

        }
        return render(request, "index.html", context)
def home(request):
        context ={

        }
        return render(request, "home.html", context)


def contact(request):
        context ={

        }
        return render(request, "contact.html", context)
def test(request):
        context ={

        }
        return render(request, "test.html", context)

def ticket(request):
          form= CreateUserForm( )  

          if request.method =='POST':
                form = CreateUserForm(request.POST )
                if form.is_valid():
                        form.save()
          context ={'form':form}
          return render(request, "ticket.html", context)
def logoutUser(request):
    logout(request)
    return redirect('index')
       

