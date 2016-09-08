from django.contrib import admin
from .models import Band

class BandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Band,BandAdmin)
# Register your models here.
