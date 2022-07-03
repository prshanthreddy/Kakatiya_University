from django.contrib import admin

# Register your models here.
from home.models import Applications, Approved, Authenticate, BOSFill, Examiner,OfficeAuthenticates
admin.site.register(Applications)
admin.site.register(Approved)
admin.site.register(Authenticate)
admin.site.register(Examiner)
admin.site.register(BOSFill)
admin.site.register(OfficeAuthenticates)
