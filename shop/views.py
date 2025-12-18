from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product
from .forms import ProductForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
    ordering = ['title']

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products') 
    else:
        form = ProductForm()
    
    data = {'form': form}
    return render(request, 'shop/create_product.html', data)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail_view.html'
    context_object_name = 'product'

@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'shop/update.html'
    form_class = ProductForm
    success_url = reverse_lazy('products')

@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')
    