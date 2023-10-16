from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bejai(request):
    return HttpResponse('electricity Bills')