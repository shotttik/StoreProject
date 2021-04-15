from django.db.models import IntegerChoices


class Cover(IntegerChoices):
    solid = 1, 'მაგარი'
    soft = 2, 'რბილი'
    super = 3, 'სუპერი'
    solid_super = 4, 'მაგარი + სუპერი'
