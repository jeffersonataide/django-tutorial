from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, you are at the pools index.')

# Create your views here.
