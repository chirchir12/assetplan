from django.contrib import admin

from .models import Career


class CareerAdmin(admin.ModelAdmin):
	list_display = ('email', 'firstname', 'lastname', 'phone','location', 'education' )
	list_filter = ('uploaded_at',)
	search_fields = ['email']


admin.site.register(Career, CareerAdmin)