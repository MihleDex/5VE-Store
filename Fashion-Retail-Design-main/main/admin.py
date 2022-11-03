from django.contrib import admin
from .models import Items, NewsLetter, UserItem
# Register your models here.

admin.site.register(Items)
admin.site.register(NewsLetter)
admin.site.register(UserItem)