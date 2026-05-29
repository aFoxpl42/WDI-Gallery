from django.db import models

class Artwork(models.Model):
    SEMESTERS = [
        ('sem3', 'Semestr 3'),
        ('sem4', 'Semestr 4'),
    ]

    title = models.CharField(max_length=200, verbose_name="Tytuł pracy")
    author = models.CharField(max_length=100, verbose_name="Autor (Imię i nazwisko)")
    semester = models.CharField(max_length=10, choices=SEMESTERS, verbose_name="Semestr")
    youtube_id = models.CharField(max_length=20, verbose_name="ID wideo z YouTube (np. WhWc3b3KhnY)")
    description = models.TextField(verbose_name="Opis projektu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        verbose_name = "Praca studencka"
        verbose_name_plural = "Prace studenckie"