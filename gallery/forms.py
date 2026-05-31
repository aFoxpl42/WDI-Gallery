from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'author', 'semester', 'image', 'video', 'youtube_link']
        
        labels = {
            'title': 'Tytul pracy',
            'author': 'Autor (Imie i Nazwisko)',
            'image': 'Obraz',
            'video': 'Wideo',
            'youtube_link':'ID wideo z YouTube (np. WhWc3b3KhnY)',
        }

    def clean_youtube_link(self):
        data = self.cleaned_data.get('youtube_link')
        if not data:
            return data
        
        if len(data) != 11:
            raise forms.ValidationError("Nieprawidlowe ID. ID wideo z YouTube musi miec 11 znakow.")
        
        if " " in data:
            raise forms.ValidationError("Nieprawidlowe ID. ID wideo z YouTube nie moze miec spacji.")
        
        return data

    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get('video')
        youtube_link = cleaned_data.get('youtube_link')

        # Rule 1: They uploaded both
        if video and youtube_link:
            raise forms.ValidationError("Please provide either a video file OR a YouTube link, not both.")
            
        # Rule 2: They uploaded neither
        if not video and not youtube_link:
            raise forms.ValidationError("You must provide either an animation file or a YouTube link.")

        return cleaned_data
    
