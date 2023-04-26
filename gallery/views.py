from django.shortcuts import render

def index(request):
    gallery_data = {
    1: {
        "name": "Carina Nebula",
        "caption": "webbtelescope.org / NASA / James Webb",
       },
    2: {
       "name": "NGC 1079 Galaxy",
       "caption": "nasa.org / NASA / Hubble", 
       },
    }
    
    return render(request, 'gallery/index.html', {
        "cards": gallery_data
    })

def image(request):
    return render(request, 'gallery/imagem.html')