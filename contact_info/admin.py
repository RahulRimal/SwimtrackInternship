from django.contrib import admin
from contact_info.models import ContactInfo
# Register your models here.

admin.site.site_header ='Welcome to Swimtrack !!'
admin.site.index_title = 'Swimtrack ContactInfo'


admin.site.register(ContactInfo)
