from django.contrib import admin
from .models import package,booking,Msg

# Register your models here.

admin.site.register(package)
admin.site.register(booking)
admin.site.register(Msg)
