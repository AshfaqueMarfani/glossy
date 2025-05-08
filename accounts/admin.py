from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_town_or_city', 'default_country')
    search_fields = ('user__username', 'user__email')


admin.site.register(UserProfile, UserProfileAdmin)
