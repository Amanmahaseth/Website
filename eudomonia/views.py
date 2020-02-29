from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,  'index.html')

def communicable(request):
    return render(request, 'communicable.html')

