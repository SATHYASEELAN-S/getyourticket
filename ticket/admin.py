from django.contrib import admin
from ticket.models import BusInfo,Stop,Travelinfo
# Register your models here.
admin.site.register(BusInfo)
admin.site.register(Travelinfo)

admin.site.register(Stop)