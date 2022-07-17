"""    <!--=====================================
       devopled by fabin ziyad
       github: https://github.com/fabin-ziyad
    ==========================================-->"""

from django.contrib import admin
from . models import Url
# Register your models here.
class displaylink(admin.ModelAdmin):
    list_display = ('link','uuid')
admin.site.register(Url,displaylink)