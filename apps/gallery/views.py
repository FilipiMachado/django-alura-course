from django.shortcuts import render, get_object_or_404, redirect

from apps.gallery.models import Photograph

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in!")
        return redirect('login')
    
    photos = Photograph.objects.order_by('date').filter(published=True)
    
    return render(request, 'gallery/index.html', {
        "cards": photos
    })

def image(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'gallery/imagem.html', {
        "photograph": photograph
    })
    
def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in!")
        return redirect('login')
    
    photos = Photograph.objects.order_by('date').filter(published=True)
    
    if 'search' in request.GET:
        name_to_search = request.GET['search']
        if name_to_search:
            photos = photos.filter(name__icontains=name_to_search)
    
    return render(request, 'gallery/buscar.html', {
        'cards': photos,
    })

def new_image(request):
    pass

def edit_image(request):
    pass

def delete_image(request):
    pass