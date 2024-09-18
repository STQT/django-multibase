from django.contrib import admin
from .models import SecondAppModel

@admin.register(SecondAppModel)
class SecondAppModelAdmin(admin.ModelAdmin):
    ...