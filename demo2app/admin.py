from django.contrib import admin

from demo2app.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(PaymentType)
admin.site.register(RequestType)
admin.site.register(Request)
admin.site.register(RequestStatus)
