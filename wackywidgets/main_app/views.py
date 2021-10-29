from django.shortcuts import render,redirect
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum
# Create your views here.

def home(request):
    widget= Widget.objects.all()
    widget_form = WidgetForm()
    return render(request,'index.html',{
      'widget':widget,
      'widget_form':widget_form
  })

def  add(request):
    form = WidgetForm(request.POST)
    new_widget = form.save()
    # total = Widget.objects.annotate(Sum('quanitity'))
    return redirect('home')




def delete(request,wdg_id):
    del_widget = Widget.objects.get(id=wdg_id)
    print(f'this is the one we want to DELETE,{del_widget}')
    del_widget.delete()
    return redirect('home')