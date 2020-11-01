from django.contrib import admin
from blog.models import Category, Post, SubCategory

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'status')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
