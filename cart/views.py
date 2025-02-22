from django.shortcuts import render
from django.http import HttpResponse

def cart_home(request):
    return HttpResponse("This is the Cart page.")

