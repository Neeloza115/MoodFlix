from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    release_date = models.DateField(null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    mood = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.mood})"