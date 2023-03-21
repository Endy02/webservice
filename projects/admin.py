from django.contrib import admin
from django.db import models

from projects.models import Project, ProjectImage


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin,]
    search_fields = ('created_at',)
    list_filter = ('created_at',)
    list_display = ('id', 'title', 'slug', 'created_at', 'updated_at')
    ordering = ("-created_at",)
    fieldsets = (
        (None, {'fields': ('title', 'description', 'short_desc')}),
        ('General', {'fields': ('link', 'thumbnail', 'slug')})        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'description', 'short_desc', 'link', 'thumbnail', 'slug')}
         ),
    )
