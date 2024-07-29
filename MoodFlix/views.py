import requests
from django.conf import settings
from django.shortcuts import render
from .forms import MoodForm

# Mapping of moods to TMDb genre IDs
MOOD_GENRE_MAP = {
    'happy': '35',     # Comedy
    'sad': '18',       # Drama
    'exciting': '28',  # Action
    'romantic': '10749', # Romance
    'All': None
}

def get_movies_by_mood(mood, language, country):
    genre_id = MOOD_GENRE_MAP.get(mood)
    
    # Base URL without genre filtering
    url = (
        f'https://api.themoviedb.org/3/discover/movie?api_key={settings.TMDB_API_KEY}'
        f'&with_original_language={language}'
        f'&region={country}'
    )

    # Add genre filtering if mood is not 'All'
    if genre_id:
        url = f'{url}&with_genres={genre_id}'
    
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json().get('results', [])
        return [
            {
                'title': movie['title'],
                'overview': movie['overview'],
                'release_date': movie['release_date'],
                'poster_path': movie.get('poster_path'),
                'vote_average': round(movie['vote_average'], 1)
            }
            for movie in movies
        ]
    else:
        # Optionally log the error
        return []

def index(request):
    form = MoodForm()
    return render(request, 'MoodFlix/index.html', {'form': form})

def results(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['mood']
            language = form.cleaned_data['language']
            country = form.cleaned_data['country']

            movies = get_movies_by_mood(mood, language, country)
            return render(request, 'MoodFlix/results.html', {'movies': movies, 'selected_mood': mood, 'language': language, 'country': country})
        
    return render(request, 'MoodFlix/index.html', {'form': MoodForm()})