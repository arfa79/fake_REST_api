from django.contrib import admin
from .models import Item
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
admin.site.register(Item)

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('get_token',)
def get_token (self , instance) :
    token , created = Token.objects.get_or_create(user=instance)
    return token.key
get_token.short_descreaption = 'Token'
admin.site.unregister(User)
admin.site.register(User , CustomUserAdmin)

