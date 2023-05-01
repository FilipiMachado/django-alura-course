from django.shortcuts import render, get_object_or_404, redirect

from apps.gallery.models import Photograph
from apps.gallery.forms import PhotoForm

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
    return render(request, 'gallery/image.html', {
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
    
    return render(request, 'gallery/search.html', {
        'cards': photos,
    })

def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in!")
        return redirect('login')
    
    form = PhotoForm
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New image registered!')
            return redirect('index')
            
    return render(request, 'gallery/new-image.html', {
        'form': form
    })

def edit_image(request, photo_id):
    photo = Photograph.objects.get(id=photo_id)
    form = PhotoForm(instance=photo)
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated successfully!')
            return redirect('index')
    
    return render(request, 'gallery/edit-image.html', {
        'form': form,
        'photo_id': photo_id
    })

def delete_image(request, photo_id):
    photo = Photograph.objects.get(id=photo_id)
    photo.delete()
    messages.success(request, 'Image deleted successfully!')
    
    return redirect('index')
    