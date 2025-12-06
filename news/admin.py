from django.contrib import admin

from .models import News


# Register your models here.


@admin.register(News)

class NewsAdmin(admin.ModelAdmin):
    list_display=('Title','created_at')
    list_filter=('Source',)
    search_fields=('Title','Content')
    
    


