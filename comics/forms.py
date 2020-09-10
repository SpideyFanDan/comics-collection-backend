from django import forms
from .models import ComicBook


class ComicBookForm(forms.ModelForm):

    class Meta:
        model = ComicBook
        fields = ('title', 'issue', 'publication_date',
                  'cover_url', 'personal_image', 'notes')
