from django.db import models


class Company(models.Model):
    name = models.CharField(verbose_name='Company Name', max_length=200)
    address = models.CharField(verbose_name='Company Address', max_length=150)
    location = models.CharField(verbose_name='Company Location', max_length=100)
    mobile_phone = models.CharField(verbose_name='Mobile Phone', max_length=12)
    email = models.EmailField(verbose_name='E-Mail')
    website = models.URLField(verbose_name='Company website')
    identification_number = models.CharField(verbose_name='Company identification number', max_length=11)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name
