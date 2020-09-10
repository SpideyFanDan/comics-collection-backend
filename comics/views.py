from rest_framework import generics
from .serializers import ComicBookSerializer
from .models import ComicBook


class ComicBookList(generics.ListCreateAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer


class ComicBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer
