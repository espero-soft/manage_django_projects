from django.db import models

class Category(models.Model):
    title = models.CharField(null=True)
    description = models.CharField(null=True)
    content = models.CharField(null=True)