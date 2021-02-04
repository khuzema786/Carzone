from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    # Image thumbnail in table
    def thumbnail(self, object):        
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius: 50%" />')
    
    thumbnail.short_description = "Photo" # Thumbnail column rename
    
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date') # Display these table columns
    list_display_links = ('id', 'thumbnail', 'first_name',) # Make fieldnames clickable
    search_fields = ('first_name', 'last_name', 'designation') # Search by fieldnames
    list_filter = ('designation',) # Filter as per fieldnames, Note: If just one value in tuple then we add a trailing commma

admin.site.register(Team, TeamAdmin)
