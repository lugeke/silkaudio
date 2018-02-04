from django.contrib import admin
# Register your models here.
from .models import Audiobook, Author, History

admin.site.register(Audiobook)
admin.site.register(Author)
admin.site.register(History)
