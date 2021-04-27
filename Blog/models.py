from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=600)

    linkV = models.URLField(default="https://docs.python.org/3/", max_length=100,null=False, blank=False)
    ChannelV = models.URLField(default="https://docs.python.org/3/", max_length=100, null=False, blank=False)
    PlaylistV = models.URLField(default="https://docs.python.org/3/", max_length=100, null=False, blank=False)

    # date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)

    image = models.ImageField(default='postdefault.jpg', upload_to='post_pics')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} , {self.author} , {self.content}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
