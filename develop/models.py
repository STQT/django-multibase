from django.db import models


class SecondAppModel(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=200)