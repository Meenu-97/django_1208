from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
     return HttpResponse("Welcome to first app!")
def firstapp_home(request):
     return HttpResponse("Welcome to MyApp!")


