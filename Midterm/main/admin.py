from django.contrib import admin
from .models import Journal, Book, Profile
# Register your models here.
admin.site.register(Journal)
admin.site.register(Book)
admin.site.register(Profile)
