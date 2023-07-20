from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def japan(request):
    return HttpResponse('japan capital  is Tokyo')
def Tokyo(request):
    return HttpResponse('cherry bloomsemms')