from rest_framework import generics, status
from .serializers import ComicBookSerializer
from .models import ComicBook
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class ComicBookList(generics.ListCreateAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer


class ComicBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComicBook.objects.all()
    serializer_class = ComicBookSerializer
    parser_class = (FileUploadParser,)

    def post(self, request, pk, *args, **kwargs):
        comicbook = get_object_or_404(Post, pk=pk)
        file_serializer = ComicBookSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
