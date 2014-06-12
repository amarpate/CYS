from django.contrib import admin
from .models import Recipient
# Register your models here.
class RecipientAdmin(admin.ModelAdmin):
	list_display = ('user_email', 'first_name', 'last_name', 'created')
	search_fields = ['user_email', 'first_name', 'last_name']
admin.site.register(Recipient, RecipientAdmin)