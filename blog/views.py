from django.shortcuts import render
from django.views.generic import DetailView
from .models import Blog
# Create your views here.
class ViweDetail(DetailView):
    model = Blog
    template_name = 'detail.html'