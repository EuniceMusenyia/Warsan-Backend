from django.contrib import admin
from .models import Child, Guardian

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','guardian' ,'date_of_birth', 'gender' )

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
