from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User, Audiobook, Author, History


admin.site.register(User, UserAdmin)
admin.site.register(Audiobook)
admin.site.register(Author)
admin.site.register(History)
