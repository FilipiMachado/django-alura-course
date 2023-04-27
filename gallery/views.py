from django.shortcuts import render, get_object_or_404

from gallery.models import Photograph

def index(request):
    photos = Photograph.objects.all()
    return render(request, 'gallery/index.html', {
        "cards": photos
    })

def image(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'gallery/imagem.html', {
        "photograph": photograph
    })