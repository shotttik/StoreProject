from datetime import timedelta

from django.db import models
from django.utils import timezone
from django_editorjs_fields import EditorJsTextField

from products.cover_choices import Cover


class Product(models.Model):
    name = models.CharField(verbose_name='პროდუქტის დასახელება', max_length=255)
    alias = models.CharField(verbose_name='ალიასი', max_length=10)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='ფასი', help_text='ლარი', max_digits=5, decimal_places=2,  default=0)
    discount = models.DecimalField(verbose_name='ფასდაკლება', help_text='ლარი',
                                   max_digits=4, decimal_places=2, default=0)
    savings = models.FloatField(verbose_name='დანაზოგი', help_text='%', default=0)
    quantity = models.IntegerField(verbose_name='აქციების რაოდენობა')
    start_date = models.DateField(verbose_name='აქცის დაწყების თარიღი', auto_now_add=True)
    end_date = models.DateField(verbose_name='აქციის დასრულების თარიღი', default=timezone.now() + timedelta(days=12))
    delivery = models.BooleanField(verbose_name='მიტანის სერვისი', default=False)
    isbn = models.CharField(verbose_name='ISBN კოდი', max_length=13)
    cashback = models.FloatField(verbose_name='ქეშბექი', help_text='%', default=0)
    cover = models.PositiveSmallIntegerField(choices=Cover.choices)
    number_of_pages = models.PositiveIntegerField(verbose_name='გვერდების რაოდენობა', default=0)
    language = models.CharField(verbose_name='ენა', max_length=100)
    height = models.FloatField('სიმაღლე', help_text='სმ', default=0)
    width = models.FloatField('სიგანე', help_text='სმ', default=0)
    description = EditorJsTextField(verbose_name='აღწერა')
    conditions = EditorJsTextField(verbose_name='აქციის პირობები')
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='სახელი', max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    alias = models.CharField(verbose_name='ალიასი', max_length=10)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Photo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='images/')
