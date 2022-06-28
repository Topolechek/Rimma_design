from django.db import models

class Project(models.Model):
    number = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image_cover = models.ImageField(upload_to='my_projects/images/')
    url = models.URLField(blank=True)

