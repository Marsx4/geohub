from django.contrib import admin
from .models import Service,Organization,Facility


admin.site.register(Organization)
admin.site.register(Facility)
admin.site.register(Service)