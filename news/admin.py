from django.contrib import admin
from .models import News, Tag

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =('name',)