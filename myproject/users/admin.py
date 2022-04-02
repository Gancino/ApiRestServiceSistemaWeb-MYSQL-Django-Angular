from django.contrib import admin

from users.models import User
# Register your models here.

class UserAdmin (admin.ModelAdmin):
    list_display=("id","username","email","first_name","last_name","is_staff")
    search_fields=("username","email")
admin.site.register(User, UserAdmin)