from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from products.forms import ProductForm
from products.models import Product
from user.models import User


def home(request):
    if 'only_discount' in request.GET:
        products = Product.objects.filter(end_date__gt=timezone.now())
        return render(request, 'pages/home.html', {'products': products})
    if 'show_all' in request.GET:
        products = Product.objects.filter()
        return render(request, 'pages/home.html', {'products': products})
    if 'without_discount' in request.GET:
        products = Product.objects.filter(end_date__lt=timezone.now())
        for product in products:
            if product.discount != 0:
                product.discount = 0
                product.save()
        return render(request, 'pages/home.html', {'products': products})
    products = Product.objects.all()
    return render(request, 'pages/home.html', {'products': products})


def add_product(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.savings = request.POST['discount'] / request.POST['price'] * 100
            product: Product = product_form.save(commit=False)
            product.save()
            return redirect('home')
    return render(request, 'pages/add_product.html', {'form': product_form})


def product_detailed(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'pages/product_detailed.html', {'product': product})


def buy_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_price = product.price - product.discount
    if request.POST:
        if product.quantity > 0:
            product.quantity -= 1
            product.save()
            user = User.objects.get(pk=request.user.pk)
            if user.balance >= product_price:
                user.balance -= product_price
                user.save()
                return redirect('home')
            return render(request, 'pages/buy_product.html', {'error': 'საკმარისი თანხა არ გაქვთ ანგარიშზე'})
        return render(request, 'pages/buy_product.html', {'error': 'პროდუქტი არ არის მარაგში'})
    return render(request, 'pages/buy_product.html', {'product': product,
                                                      'product_price': product_price})