from django.shortcuts import render, render_to_response, RequestContext
from django.conf import settings
from django.core.mail import send_mail

from .forms import SignUpForm
# Create your views here.

def home(request):
	#request.method you made in the html template page
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	return render_to_response('signups.html', locals(), 
			context_instance=RequestContext(request))
