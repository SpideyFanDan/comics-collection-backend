from django.db import models

# Create your models here.


class ComicBook(models.Model):
    title = models.CharField(max_length=250)
    issue = models.CharField(max_length=25)
    publication_date = models.CharField(max_length=100)
    cover_url = models.TextField()
    personal_image = models.ImageField(upload_to='images/', blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
