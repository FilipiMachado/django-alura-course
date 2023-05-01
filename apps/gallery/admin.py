from django.contrib import admin

from apps.gallery.models import Photograph

class PhotosList(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category', 'published', 'user')
    list_editable = ('published',)
    list_per_page = 10

# Register your models here.

admin.site.register(Photograph, PhotosList)
