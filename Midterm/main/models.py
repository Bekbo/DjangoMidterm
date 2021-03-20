from django.db import models


# Create your models here.
from auth_.models import User


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100, verbose_name='Book Journal Name')
    price = models.IntegerField()
    description = models.CharField(max_length=200, verbose_name='Book Journal Description')
    created_at = models.DateTimeField(verbose_name='Journal Date')

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} - {self.genre}'


class Journal(BookJournalBase):
    TYPE_CHOICE = (
        (1, "Bullet"),
        (2, "Food"),
        (3, "Travel"),
        (4, "Sport")
    )
    type = models.IntegerField(choices=TYPE_CHOICE, verbose_name='Type of Journal', default=1)
    publisher = models.CharField(max_length=100, verbose_name='Publisher')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def __str__(self):
        return f'{self.name} - {self.publisher}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - Profile'
