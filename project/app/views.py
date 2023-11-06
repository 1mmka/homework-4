from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.models import Image

# Create your views here.
class ShowImage(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images'
    
class ShowImageDetails(DetailView):
    model = Image
    template_name = 'detail.html'
    context_object_name = 'details'