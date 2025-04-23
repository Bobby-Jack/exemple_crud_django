from django.shortcuts import render, redirect
from .models import Product
from .form import ProductForm
# Create your views here.



def get_all_product(request):
    all_product = Product.objects.all()
    return render(request, "allProduct.html", {'all_product' : all_product})

def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "detailProduct.html", {'product' : product})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProductForm()
        return render(request, 'createProduct.html', {'form':form})