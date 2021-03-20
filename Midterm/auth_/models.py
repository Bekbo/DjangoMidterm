from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    ADMIN = 1
    GUEST = 2

    ROLES = (
        (ADMIN, 'Admin'),
        (GUEST, 'Guest')
    )
    role = models.PositiveSmallIntegerField(choices=ROLES, default=GUEST)

    def __str__(self):
        return f'{self.username} - {self.role}'

