from django.db.models import IntegerChoices


class Status(IntegerChoices):
    accountant = 1, 'ბუღალტერი'
    designer = 2, 'დიზაინერი'
    manager = 3, 'მენეჯერი'
    call_center = 4, 'ქოლ ცენტრი'
