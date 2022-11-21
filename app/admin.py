from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Token


class TokenInline(admin.StackedInline):
    model = Token
    readonly_fields = ('key',)
    extra = 0


UserAdmin.inlines = [TokenInline]
