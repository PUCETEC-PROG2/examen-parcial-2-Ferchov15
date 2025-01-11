from django.db import models

# Create your models here.
class Movie (models.Model):
    id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=30, null=False)
    GENRE_CHOICES = {
        ('A', 'Acción'),
        ('T', 'Terror'),
        ('C', 'Comedia'),
        ('CF', 'Ciencia Ficción'),
        ('D', 'Drama'),
        ('F', 'Fantasia'),
    }
    movie_genre = models.CharField(max_length=2, choices=GENRE_CHOICES, null=False)
    name_director = models.CharField(max_length=30, null=False)
    year_publication = models.DateField(null=True, blank=True)
    sinopsis = models.TextField()
    
    def __str__(self):
        return self.movie_title
    

