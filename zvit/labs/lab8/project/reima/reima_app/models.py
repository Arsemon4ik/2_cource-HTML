from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Catalog(models.Model):
    name_catalog = models.CharField(max_length=64)

    def str(self):
        return f'{self.name_catalog}'


class Clothes(models.Model):
    Jumpsuits = "JM"
    Costumes = 'CS'
    Jacket = 'J'
    TYPES = (
        (Jumpsuits, 'Комбинезоны'),
        (Costumes, 'Костюмы'),
        (Jacket, 'Куртки'),
    )
    name = models.CharField(max_length=64)
    what_catalog = models.CharField(choices=TYPES, max_length=3, default=None)

    description = models.TextField(max_length=228)
    catalog = models.ForeignKey(Catalog, on_delete=CASCADE)

    def str(self):
        return f'{self.name}'

# class User(User):
#     TYPES = (
#         ('ukr','Украинский'),
#         ('rus','Русский'),
#         ('us','Английский'),
#     )
#     language = models.CharField(choices=TYPES, max_length=3,default='ukr')