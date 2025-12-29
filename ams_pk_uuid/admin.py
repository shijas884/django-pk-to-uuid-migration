from django.contrib import admin
from ams_pk_uuid.models import Event,Company,AppointmentUser,Slot

# Register your models here.
admin.site.register(Event)
admin.site.register(Company)
admin.site.register(AppointmentUser)
admin.site.register(Slot)