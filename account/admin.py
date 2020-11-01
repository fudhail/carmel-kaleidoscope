from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import MyUser, Request, User



class UsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')

admin.site.register(MyUser, UserAdmin)
admin.site.register(Request)
admin.site.register(User, UsersAdmin)
