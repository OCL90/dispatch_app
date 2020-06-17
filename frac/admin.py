from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Operator)
admin.site.register(Crew)
admin.site.register(ServiceCo)
admin.site.register(Well)
admin.site.register(SandType)
admin.site.register(LoadingFacility)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Driver)
admin.site.register(Order)