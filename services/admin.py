from django.contrib import admin
from .models import Quote

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('email', 'fname', 'phone', 'message')
	list_filter = ('phone', )
	search_fields =['email']
admin.site.register(Quote, ServiceAdmin)