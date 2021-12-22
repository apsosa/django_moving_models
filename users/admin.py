from django.contrib import admin

# Register your models here.
from .models import Choice,Author,Question

admin.site.register(Author)
admin.site.register(Choice)
admin.site.register(Question)