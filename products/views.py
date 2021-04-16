import datetime

import xlwt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from products.forms import ProductForm
from products.models import Product
from user.models import User


def home(request):
    if 'only_discount' in request.GET:
        products = Product.objects.filter(end_date__gt=datetime.date.today())
        return render(request, 'pages/home.html', {'products': products})
    if 'show_all' in request.GET:
        products = Product.objects.filter()
        return render(request, 'pages/home.html', {'products': products})
    if 'without_discount' in request.GET:
        products = Product.objects.filter(end_date__lt=datetime.date.today())
        for product in products:
            if product.discount != 0:
                product.discount = 0
                product.save()
        return render(request, 'pages/home.html', {'products': products})
    products = Product.objects.all()
    return render(request, 'pages/home.html', {'products': products})


@login_required(login_url="/user/login")
def add_product(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product: Product = product_form.save(commit=False)
            product.savings = product.discount / product.price * 100
            product.save()
            return redirect('home')
    return render(request, 'pages/add_product.html', {'form': product_form})


def product_detailed(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'pages/product_detailed.html', {'product': product})


@login_required(login_url="/user/login")
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
                send_mail(subject='message for test',
                          message='some lorem ipsum',
                          from_email='test@palitra.ge',
                          recipient_list=[user.email],
                          fail_silently=False)
                return redirect('home')
            return render(request, 'pages/buy_product.html', {'error': 'საკმარისი თანხა არ გაქვთ ანგარიშზე'})
        return render(request, 'pages/buy_product.html', {'error': 'პროდუქტი არ არის მარაგში'})
    return render(request, 'pages/buy_product.html', {'product': product,
                                                      'product_price': product_price})


def export_excel(request, pk):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=Product-{pk}-' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Product')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID', 'აქციის დასახელება', 'მიმდინარე ფასი', 'ფასდაკლების პროცენტი', 'დარჩენილი რაოდენობა',
               'აქციის დასრულების თარიღი', 'ქეშბექი']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    row_num += 1
    product = Product.objects.get(pk=pk)
    columns = [product.pk, product.name, product.price, product.discount, product.quantity,
               product.end_date.isoformat(), product.cashback]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    wb.save(response)
    return response
