from django import forms

class MoodForm(forms.Form):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('exciting', 'Exciting'),
        ('romantic', 'Romantic'),
        ('All', 'All Movies')
    ]
    LANGUAGE_CHOICES = [
        ('en', 'English (Hollywood)'),
        ('hi', 'Hindi (Bollywood)'),
        # Add more languages as needed
    ]
    COUNTRY_CHOICES = [
        ('US', 'United States (Hollywood)'),
        ('IN', 'India (Bollywood)'),
        # Add more countries as needed
        # Add other regions as needed
    ]

    mood = forms.ChoiceField(choices=MOOD_CHOICES, required=True)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=True)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True)