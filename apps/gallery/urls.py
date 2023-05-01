from django.urls import path
from apps.gallery.views import index, image, search, new_image, edit_image, delete_image

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photo_id>', image, name='imagem'),
    path('search', search, name="search"),
    path('new-image', new_image, name="new_image"),
    path('edit-image', edit_image, name="edit_image"),
    path('delete-image', delete_image, name="delete_image")
]
