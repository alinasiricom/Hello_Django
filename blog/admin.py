from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title', 'author', 'counted_views', 'status', 'published_date', 'created_date']
    list_filter = ['status', 'author']
    search_fields = ['title', 'content']
    # ordering = ['-created_date']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
