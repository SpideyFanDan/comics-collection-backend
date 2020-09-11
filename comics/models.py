from django.db import models

# Create your models here.


class ComicBook(models.Model):
    title = models.CharField(max_length=250, default='Series Title...')
    issue = models.CharField(max_length=25, default='issue #...')
    publication_date = models.CharField(max_length=100, default='pub. date...')
    cover_url = models.TextField(default='url only...')
    personal_image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    notes = models.TextField(
        blank=True, null=True, default='Add any notes about comic here or leave blank')

    def __str__(self):
        return self.title
