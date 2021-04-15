from django.db.models import IntegerChoices


class Location(IntegerChoices):
    tbilisi = 1, 'თბილისი'
    region = 2, 'რეგიონი'
