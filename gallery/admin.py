from django.contrib import admin

from gallery.models import Photograph

class PhotosList(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    

# Register your models here.

admin.site.register(Photograph, PhotosList)
