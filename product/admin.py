from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.
class WatchPictureInline(admin.TabularInline):
    model = WatchPicture
    extra = 1
    fields = ("pic_num", "ph", "image_tag", "show")
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.ph:
            return mark_safe('<img src="%s" width="100px" />' % obj.ph.url)
        else:
            return ""

    image_tag.short_description = u'商品详情图'
    image_tag.allow_tags = True

class CommandInline(admin.TabularInline):
    model = Command
    extra = 1

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name",]

@admin.register(WatchProduct)
class WatchProductAdmin(admin.ModelAdmin):
    list_display = ['image_tag', 'brand', 'name', 'ori_price', 'price', 'promote']
    list_display_links = ('name',)
    readonly_fields = ('image_tag', 'promote')

    def image_tag(self, obj):
        if obj.hompic:
            return mark_safe('<img src="%s" width="100px" />' % obj.hompic.ph.url)
        else:
            return obj.hompic

    image_tag.short_description = u'首页产品图片'
    image_tag.allow_tags = True

    def promote(self, obj):
        return mark_safe('<a href="/product/{}" target="_blank">链接</a>'.format(obj.pk))
    promote.short_description = u'推广页地址'
    promote.allow_tags = True

    inlines = [WatchPictureInline, CommandInline]