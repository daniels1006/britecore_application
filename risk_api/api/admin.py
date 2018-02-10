from django.contrib import admin

from api.models import *

admin.site.register(RiskType)
admin.site.register(Risk)
admin.site.register(DataType)
admin.site.register(Field)
admin.site.register(MetaField)
admin.site.register(RiskData)
