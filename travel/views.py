from django import forms
from django.contrib.auth import login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
from .forms import CreateUserForm

def registerPage(request):
        form= CreateUserForm( )  

        if request.method =='POST':
                form = CreateUserForm(request.POST )
                if form.is_valid():
                        form.save()
                        return redirect(loginPage)
        context ={'form':form}
        return render(request, "register.html", context)
def loginPage(request):
        context ={}
        return render(request, "login.html", context)
        
def index(request):
        context ={

        }
        return render(request, "index.html", context)


def contact(request):
        context ={

        }
        return render(request, "contact.html", context)

def ticket(request):
          form= CreateUserForm( )  

          if request.method =='POST':
                form = CreateUserForm(request.POST )
                if form.is_valid():
                        form.save()
          context ={'form':form}
          return render(request, "ticket.html", context)
