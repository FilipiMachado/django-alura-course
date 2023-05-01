from django.urls import path
from apps.gallery.views import index, image, search

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photo_id>', image, name='imagem'),
    path('search', search, name="search")
]
