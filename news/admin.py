from django.contrib import admin
from .models import Article,tags

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.

admin.site.register(Article)
admin.site.register(tags)