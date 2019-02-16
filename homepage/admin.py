from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

@admin.register(HomePic)
class HomePicAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag', 'pic_num', 'show']
    readonly_fields = ('image_tag',)
    def image_tag(self, obj):
        return mark_safe('<img src="%s" width="50%%" />' % obj.ph.url)
    image_tag.short_description = u'首页产品图片'
    image_tag.allow_tags = True
