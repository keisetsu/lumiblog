from django.db import models

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()

    class Meta:
        ordering = ('created',)

# Create your models here.
