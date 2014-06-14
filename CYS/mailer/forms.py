from django import forms 

from .models import Recipient

class SignUpForm(forms.ModelForm):
	class Meta:
		model = Recipient