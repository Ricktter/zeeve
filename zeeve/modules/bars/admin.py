from django.contrib import admin
from .models import Bar

class BarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bar,BarAdmin)

# Register your models here.
