from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artwork

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
    artworks = Artwork.objects.all().order_by('-created_at')
    context = {'artworks' : artworks}
    return render(request, 'gallery/dashboard.html', context)