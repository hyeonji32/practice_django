from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=True, default="")
    password = models.CharField(max_length=255)