from django.db import models


class User(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    name = models.CharField(max_length=255, null=True, default="")
    password = models.CharField(max_length=255)
