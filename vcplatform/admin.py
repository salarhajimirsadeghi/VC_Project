from django.contrib import admin

from .models import VC_data, Companies, VC_Company

admin.site.register(VC_data)
admin.site.register(Companies)
admin.site.register(VC_Company)

# Register your models here.
