from django.db import models

from django.core.mail import EmailMessage, EmailMultiAlternatives, get_connection
from post_office import mail
from post_office.validators import validate_email_with_name

from django.db.models.signals import pre_delete 
from django.dispatch import receiver
# Create your models here.

SENDER = "Devstein@seas.upenn.edu"
CONTACT_LIST = [] 
EMAIL_LIST = [] 

class RecipientManager(models.Manager):
	"""
	A model to control the mail list
	"""
	
	def mailAll(self):
		pass

class Recipient(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	user_email = models.EmailField(max_length=254, validators=[validate_email_with_name] )
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	
	def subscribe(self):
		EMAIL_LIST.append(self.user_email.lower())
		CONTACT_LIST.append([self.first_name.lower(), self.last_name.lower()])

	def save(self, *args, **kwargs):
		#Have to create check to see if recipient already exists 
		if (self.user_email.lower() not in EMAIL_LIST):
			#Place to do something with recipients
			self.subscribe()
			#Add success comfirmation 
			return super(Recipient, self).save(*args, **kwargs)
		else:
			pass
		#Add else statement with error message



	@receiver(pre_delete, sender=RecipientManager)
	def unsubscribe(sender, instance, **kwargs):
		#Check to see if email exists
		if (self.user_email.lower() in EMAIL_LIST):
			EMAIL_LIST.remove(self.user_email.lower())
			CONTACT_LIST.remove([self.first_name.lower(), self.last_name.lower()])
			#Add successfully removed from email list   
		else:
			pass
		#Add else statement for error message 

	def __unicode__(self):
		return self.user_email
	
