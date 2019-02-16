from django.db import models

from homepage.models import HomePic

# Create your models here.

class Brand(models.Model):
    name = models.CharField(u'品牌', max_length=256)

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = "品牌"

    def __str__(self):
        return self.name



class WatchProduct(models.Model):
    hompic = models.OneToOneField(HomePic, on_delete=models.CASCADE, blank=True, null=True, verbose_name="主页图")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="品牌")
    #ph = models.ImageField(u'图片', upload_to='watch')
    name = models.CharField(u'名称', max_length=256)
    ori_price = models.CharField(u'原价格', max_length=256)
    price = models.CharField(u'现价格', max_length=256)

    class Meta:
        ordering = ['brand', 'name']
        verbose_name = "型号列表"
        verbose_name_plural = "型号列表"
    def __str__(self):
        return self.name

class WatchPicture(models.Model):
    watchproduct = models.ForeignKey(WatchProduct, on_delete=models.CASCADE)
    ph = models.ImageField(u'图片', upload_to='watchPicture')  # 多图
    pic_num = models.IntegerField(u'排序', default=0)
    show = models.BooleanField(u'显示', default=True)
    class Meta:
        ordering = ['pic_num']
        verbose_name = "详情页图片"
        verbose_name_plural = "详情页图片"

class Command(models.Model):
    product = models.ForeignKey(WatchProduct, on_delete=models.CASCADE)
    name = models.CharField(u'评论人', max_length=256)
    tel_num = models.CharField(u'电话', max_length=128)
    address = models.CharField(u'地址', max_length=128)
    content = models.TextField(u'内容',help_text='单个评论不要超过500字', max_length=512)
    #ph = models.ImageField(u'晒图', upload_to='command')#多图
    class Meta:
        #ordering = ['pic_num']
        verbose_name = "商品评论"
        verbose_name_plural = "商品评论"
