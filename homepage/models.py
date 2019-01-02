from django.db import models

# Create your models here.

class Order(models):
    ip = models.GenericIPAddressField()


class Production(models):
    name = models.CharField()
    title = models.CharField()
    pic_list = models.


class Comment(models):
    content = models.CharField()
    # picture = models


class Picture(models):
    pic_num = models.ImageField()