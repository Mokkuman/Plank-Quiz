from atexit import register
from django.contrib import admin

# Register your models here.
from .models import User,Flashcard
admin.site.register(User)
admin.site.register(Flashcard)