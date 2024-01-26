from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Family(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='имя')
    second_name = models.CharField(max_length=20, verbose_name='фамилия')

    def __str__(self):
        return f"{self.first_name}-{self.second_name}"

    class Meta:
        ordering = ['id']


class User(AbstractUser):
    USER = "user"
    MANAGER = "manager"
    CRM_ADMIN = "CRM_admin"

    CHOICES = (
        (USER, 'user'),
        (MANAGER, 'manager'),
        (CRM_ADMIN, 'CRM_admin'),
    )

    status_user = models.CharField(
        max_length=15,
        choices=CHOICES,
        default=CHOICES[0],
    )

    class Meta:
        ordering = ('pk', 'username',)  # сортировка таблицы при ее отображении
