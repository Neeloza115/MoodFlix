from django.contrib import admin 

from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "description", "poster_url", "mood", "language", "country")
