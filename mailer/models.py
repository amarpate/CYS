from django.db import models

from django.core.mail import EmailMessage, EmailMultiAlternatives, get_connection
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


	def mailAll(self):
		pass

class Recipient(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	user_email = models.EmailField(max_length=254, validators=[validate_email_with_name] )
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	

	def __unicode__(self):
		return self.user_email
	
	recipients = RecipientManager() 

	