from django.contrib import admin
from blog.models import Category, Post, SubCategory

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'date', 'status')

class SubAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, SubAdmin)
