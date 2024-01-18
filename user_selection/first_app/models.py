from django.db import models


# Create your models here.

class Family(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='имя')
    second_name = models.CharField(max_length=20, verbose_name='фамилия')

    def __str__(self):
        return f"{self.first_name}-{self.second_name}"
