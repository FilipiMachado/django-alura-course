from django.db import models

from datetime import datetime

# Create your models here.

class Photograph(models.Model):
    
    CATEGORY_OPTIONS = [
        ("NEBULA", "Nebula"),
        ("STAR", "Star"),
        ("GALAXY", "Galaxy"),
        ("PLANET", "Planet")
    ]
    
    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=100, null=False, blank=False)
    published = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return f"Photograph [name={self.name}]"