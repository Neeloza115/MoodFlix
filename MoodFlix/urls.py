from django.urls import path
from .views import index, results

urlpatterns = [
    path('', index, name='index.html'),  # Maps to index view for displaying the form
    path('results', results, name='results.html'),  # Maps to results view for displaying movie recommendations
]