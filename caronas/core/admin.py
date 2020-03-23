from django.contrib import admin
from .models import Passengers


class PassengersAdmin(admin.ModelAdmin):

    list_display = ['name', 'address', 'phone', 'photo', 'evaluation', 'obs']
    search_fields = ['name', 'phone']
    list_filter = ['name', 'phone']


admin.site.register(Passengers, PassengersAdmin)
