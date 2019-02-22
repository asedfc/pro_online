from django.db import models

# Create your models here.
'''
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
'''


class HomePic(models.Model):
    ph = models.ImageField(u'图片', upload_to='homepic')
    name = models.CharField(u'名称', max_length=256)
    click_href = models.CharField(u'商品链接', max_length=256, blank=True, null=True)
    pic_num = models.IntegerField(u'排序')
    show = models.BooleanField(u'显示', default=True)

    class Meta:
        ordering = ['pic_num']
        verbose_name = "首页图片"
        verbose_name_plural = "首页图片"

    def __str__(self):
        return self.name


class Carousel(models.Model):
    ph = models.ImageField(u'轮播图片', upload_to='carousel')
    name = models.CharField(u'名称', max_length=256)
    click_href = models.CharField(u'轮播商品链接', max_length=256, blank=True, null=True)
    pic_num = models.IntegerField(u'排序')
    show = models.BooleanField(u'显示', default=True)

    class Meta:
        ordering = ['pic_num']
        verbose_name = "首页轮播图片"
        verbose_name_plural = "首页轮播图片"

    def __str__(self):
        return self.name

