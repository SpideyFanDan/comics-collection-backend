from rest_framework import serializers
from .models import ComicBook


class ComicBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicBook
        fields = ('title', 'issue', 'publication_date',
                  'cover_url', 'personal_image', 'notes')
