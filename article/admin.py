from django.contrib import admin

# Register your models here.
from .models import Post,Blog, Entry
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Post)