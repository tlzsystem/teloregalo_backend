from django.contrib import admin
from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id','user_creator','status','publish_date','title','description')


admin.site.register(Publication, PublicationAdmin)