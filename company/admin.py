from django.contrib import admin
from .models import Company


@admin.register(Company)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
