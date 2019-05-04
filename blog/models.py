from django.db import models
from django.contrib.auth.models import User


class Blogs(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', blank=True, upload_to='images')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def des_snippet(self):
        return self.description[:30] + '....See more'
