from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView
from .models import Product

# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'    
