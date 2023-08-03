from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __init__(self, user_id, password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.password = password
