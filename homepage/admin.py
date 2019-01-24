from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(HomePic)
class HomePicAdmin(admin.ModelAdmin):
    list_display = ['name', 'ph', 'pic_num', 'show']
    def image_tag(self):
        url = self.urls
        return u'<img src="%s" />' % url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    pass