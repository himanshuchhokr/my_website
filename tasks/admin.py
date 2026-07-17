from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'status', 'commit_hash', 'created_at')
    list_filter = ('status', 'tag')
    search_fields = ('title',)
