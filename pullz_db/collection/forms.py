from django import forms
from .models import Comic

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'issue_number', 'release_date', 'coverType', 'condition',
                  'writer', 'artist', 'publisher', 'status']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }