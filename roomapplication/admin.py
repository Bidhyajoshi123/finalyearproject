from django.contrib import admin
from .models import Room, Rating


# Register your models here.

@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ['location', 'image', 'description']
    search_fields = ['location']


@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
    list_display = ['user', 'location', 'rating']
