from django.db import models
from django.core.mail import EmailMessage, EmailMultiAlternatives, get_connection
from post_office import mail
from post_office.validators import validate_email_with_name

# Create your models here.

SENDER = "Devstein@seas.upenn.edu"
CONTACT_LIST = {} 
EMAIL_LIST =  [] 

class Recipient(models.Model):

	"""
	A model to control the mail list
	"""

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	user_email = models.EmailField(max_length=254, validators=[validate_email_with_name] )
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	def subscribe(self):
		#Check to see if email exists 
		if (self.user_email.lower() not in EMAIL_LIST):
			#Add email to EMAIL_LIST and add new contact info to CONTACT_LIST
			EMAIL_LIST.append(self.user_email.lower())
			CONTACT_LIST[self.user_emal.lower()] = tuple(self.first_name.lower(), self.last_name.lower())

			#Add successful addition comfirmation  

		#Add else statement for error message
		
	def unsubscribe(self):
		#Check to see if email exists
		if (self.user_email.lower() in EMAIL_LIST):
			EMAIL_LIST.remove(self.user_email.lower())
			del CONTACT_LIST[self.user_email.lower()]
			#Add successfully removed from email list   

		#Add else statement for error message 

	def mailAll(self):
		pass
