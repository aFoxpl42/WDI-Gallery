from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artwork
from .forms import ArtworkForm

def home_page(request):
    artworks_from_db = Artwork.objects.all().order_by('-created_at')
    
    context = {
        'artworks': artworks_from_db
    }
    return render(request, 'gallery/index.html', context)

class CustomLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, f"Logowanie poprawne, {form.get_user().username}")
        return super().form_valid(form)
    
@login_required(login_url='login')
def dashboard_view(request):
    artworks = Artwork.objects.filter(owner=request.user).order_by('-created_at')
    context = {'artworks' : artworks}
    return render(request, 'gallery/dashboard.html', context)

@login_required(login_url='login')
def add_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.owner = request.user
            artwork.save()
            messages.success(request, "Praca dodana.")
            return redirect('dashboard')
    else:
        form = ArtworkForm()
    context = {'form' : form}
    return render(request, 'gallery/add_artwork.html', context)

@login_required(login_url='login')
def edit_artwork(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArtworkForm(instance=artwork)
        
    context = {'form' : form, 'artwork':artwork}
    return render(request, 'gallery/edit_artwork.html', context)

@login_required(login_url='login')
def delete_artwork(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk, owner=request.user)
    if request.method == 'POST':
        artwork.delete()
        return redirect('dashboard')
    
    context = {'artwork' : artwork}
    return render(request, 'gallery/delete_artwork.html', context)