from django.contrib import admin
from .models import Interest

class InterestAdmin(admin.ModelAdmin):
    list_display = ('id','publication_id','user_interest')

admin.site.register(Interest, InterestAdmin)
