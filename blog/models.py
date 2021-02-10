from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, default='')
    context = models.TextField()
    img = models.ImageField(upload_to='static/img', default='')

    def __str__(self):
        return self.title