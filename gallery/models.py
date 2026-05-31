from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Artwork(models.Model):
    SEMESTERS = [
        ('sem3', 'Semestr 3'),
        ('sem4', 'Semestr 4'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, verbose_name="Tytuł pracy")
    author = models.CharField(max_length=100, verbose_name="Autor (Imię i nazwisko)")
    semester = models.CharField(max_length=10, choices=SEMESTERS, verbose_name="Semestr")
    image = models.ImageField(upload_to='artworks/images', null=True, blank=True)
    video = models.FileField(
        upload_to='artworks/videos', 
        null=True, 
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    youtube_link = models.CharField(max_length=20, verbose_name="ID wideo z YouTube (np. WhWc3b3KhnY)", null=True, blank=True)
    description = models.TextField(verbose_name="Opis projektu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        verbose_name = "Praca studencka"
        verbose_name_plural = "Prace studenckie"
        
        
        
# TODO: jonskid access to everything - superuser - admin
# TODO: user change password
# TODO: maybe adding group of users with same permissions - teachers // kind of pointless tho
# TODO: connecting 'prowadzacy' on home_page with users
# TODO: adding info about teacher when opening animation from gallery
# TODO: RESPOSNSIVE DESIGN!!!
# TODO: ??? new features maybe
# TODO: hosting - last step
# TODO: updating docs