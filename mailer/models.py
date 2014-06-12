from django.db import models

from django.core.mail import EmailMessage, EmailMultiAlternatives, get_connection, send_mail
from post_office import mail
from post_office.validators import validate_email_with_name

from django.db.models.signals import pre_delete 
from django.dispatch import receiver
# Create your models here.

SENDER = "Devstein@seas.upenn.edu"

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
		for emailaddress in email_list:
			email = {
				'sender' : SENDER,
				'recipients' : emailaddress,
				'subject' : 'Welcome!',
				'message' : 'Thank you for joining the CYS Community'
			}
			messages.append(email)
		mail.send_many(messages)

	def mail_all2(self):
		send_mail('Welcome', 'Thank you for joining the CYS Community', SENDER, self.get_emails(),
				fail_silently = False, auth_user='Devstein', auth_password='WTFisthis645')
		

class Recipient(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	user_email = models.EmailField(max_length=254, validators=[validate_email_with_name] )
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	

	def __unicode__(self):
		return self.user_email
	
	recipients = RecipientManager() 

	