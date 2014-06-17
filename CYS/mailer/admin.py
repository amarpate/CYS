from django.contrib import admin
from .models import Recipient
# Register your models here.
class RecipientAdmin(admin.ModelAdmin):
	list_display = ('your_email', 'first_name', 'last_name', 'created', 'updated')
	search_fields = ['your_email', 'first_name', 'last_name']
		
admin.site.register(Recipient, RecipientAdmin)