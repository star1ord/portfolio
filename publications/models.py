from django.db import models
class Publications(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=2000)
