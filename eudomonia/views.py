from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,  'index.html')
<<<<<<< HEAD
=======

def communicable(request):
    return render(request, 'communicable.html')

>>>>>>> 5517c7ec4ce7ccd291c84a9a2330fae103817b83
