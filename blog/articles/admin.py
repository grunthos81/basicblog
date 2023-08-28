from django.contrib import admin
from .models import *

class SectionAdmin(admin.ModelAdmin):
    ordering = list_display = search_fields = ('section_name',)

class ArticleAdmin(admin.ModelAdmin):
    ordering = ('title', 'section', 'last_edited')
    list_display = ('title', 'draft', 'last_edited', 'section')
    search_fields = ('title', 'section')

admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)



