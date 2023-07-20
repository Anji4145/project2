from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def greetings(request):
    return HttpResponse('good morning')
def india(request):
    return HttpResponse('capital of india is Delhi')
