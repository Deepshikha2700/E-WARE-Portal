from django.contrib import admin
from login.models import Contact
from login.models import Profile
from login.models import Phishing,Date_user
# from login.models import Template_Category

# Register your models here.
admin.site.site_header="E-WARE PORTAL"
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Phishing)
admin.site.register(Date_user)


