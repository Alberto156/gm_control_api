from django.contrib import admin
from .models import Team

@admin.register(Team)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'company'
    )
