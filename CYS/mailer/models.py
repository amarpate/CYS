from django.db import models
from django.core.mail import send_mail
from django.utils.encoding import smart_unicode


# Create your models here.

SENDER = "campusyardsale2@gmail.com"

class RecipientManager(models.Manager):
	"""
	A model to control the mail list
	"""
	def get_emails(self):
		email_list = [] 
		for email in self.all():
			email_list.append(str(email.your_email))
		return email_list

	def get_names(self):
		names_list = []
		for name in self.all():
			names_list.append([str(name.first_name),str(name.last_name)])
		return names_list

	def mail_all(self):
		email_list = self.get_emails()
		mail.send_mail('Welcome!', 'Thank you for joining the CYS Community!', 
						SENDER, email_list)
					
class Recipient(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	your_email = models.EmailField(max_length=254)
	created = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, db_index=True)

	def __unicode__(self):
		return smart_unicode(self.your_email)
	
	objects = RecipientManager() 

	