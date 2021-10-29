from django.shortcuts import render
from .models import Widget

# Create your views here.

def home(request):
    widget= Widget.objects.all()
    return render(request,'index.html',{
      'widget':widget
  })