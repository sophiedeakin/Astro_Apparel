from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):
    """" A view to return the index page """
    
    return render(request, 'home/index.html')

