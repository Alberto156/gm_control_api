from django.contrib import admin
from .models import User, Roles
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'username'
    )


@admin.register(Roles)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "name"
    )
