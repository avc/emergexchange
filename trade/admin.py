from __future__ import unicode_literals

from django.contrib import admin
# from .models import Profile
from .models import *

class GoodModelAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "user", "value"]
    list_display_links = ['name']
    list_filter = ['modified']
    search_fields = ['name']
    class Meta:
        model = Good

class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "phone_number"]
    list_display_links = ['user']
    search_fields = ['user']
    class Meta:
        model = UserInfo

class NeedModelAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "user", "modified", "value"]
    # list_display_links = ['user']
    # search_fields = ['user']
    class Meta:
        model = Need

admin.site.register(Good, GoodModelAdmin)
admin.site.register(Need, NeedModelAdmin)
admin.site.register(UserInfo, UserInfoModelAdmin)
