from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    POST_TYPES = (
        ('C', 'Contenido'),
        ('E', 'Evento'),
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    post_type = models.CharField(max_length=1, choices=POST_TYPES, default='C')
    event_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.post_type == 'C':
            self.event_date = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')