from django.db import models
from django.utils import timezone
# Create your models here.
class news_db(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length = 30)
    content = models.TextField()
    