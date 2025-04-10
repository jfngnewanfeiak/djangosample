from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField("title",max_length=200)
    text = models.TextField("main sentence...")
    date = models.DateTimeField("date", default=timezone.now)

    def __str__(self):
        return self.title