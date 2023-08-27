from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('token_key',)
    
    def token_key(self, instance):
        token, created = Token.objects.get_or_create(user=instance)
        return token.key
    
    token_key.short_description = 'Token'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
