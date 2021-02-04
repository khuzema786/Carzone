from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    # Image thumbnail in table
    def thumbnail(self, object):
        return format_html(f'<img src="{object.car_photo.url}" width="40" style="border-radius: 50px;" />')
    
    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured') # Display these table columns
    list_display_links = ('id', 'thumbnail', 'car_title') # Make fieldnames clickable
    list_editable = ('is_featured',) # Makes is_featured editable 
    search_fields = ('id', 'car_title', 'model', 'body_style', 'fuel_type') # Search by fieldnames
    list_filter = ('city', 'model', 'body_style', 'fuel_type') # Filter as per fieldnames

admin.site.register(Car, CarAdmin)