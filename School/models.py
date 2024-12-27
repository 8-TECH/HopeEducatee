from django.db import models


class School(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
