from django.db import models
from django.core.mail import EmailMessage, EmailMultiAlternatives, get_connection, send_mail
from django.db.models.signals import pre_delete 
from django.dispatch import receiver

from post_office import mail
from post_office.validators import validate_email_with_name

# Create your models here.

SENDER = "campusyardsale2@gmail.com"

class RecipientManager(models.Manager):
	"""
	A model to control the mail list
	"""
	def get_emails(self):
		email_list = [] 
		for email in self.all():
			email_list.append(str(email.user_email))
		return email_list

	def get_names(self):
		names_list = []
		for name in self.all():
			names_list.append([str(name.first_name),str(name.last_name)])
		return names_list

	def mail_all(self):
		messages = []
		email_list = self.get_emails()
		email = {
				'sender' : SENDER,
				'recipients' : email_list,
				'subject' : 'Welcome!',
				'message' : 'Thank you for joining the CYS Community'
			}
		mail.send(email_list,SENDER,subject='Welcome2CYS!',
					message='Thank you for joining the CYS Community',
					priority='now')
					

class Recipient(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	user_email = models.EmailField(max_length=254, validators=[validate_email_with_name] )
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	

	def __unicode__(self):
		return self.user_email
	
	recipients = RecipientManager() 

	