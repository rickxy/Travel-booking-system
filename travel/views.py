from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
        context ={

        }
        return render(request, "index.html", context)


def contact(request):
        context ={

        }
        return render(request, "contact.html", context)