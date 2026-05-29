from django.shortcuts import render
from .models import Artwork

def home_page(request):
    artworks_from_db = Artwork.objects.all().order_by('-created_at')
    
    context = {
        'artworks': artworks_from_db
    }
    return render(request, 'gallery/index.html', context)