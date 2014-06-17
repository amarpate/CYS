from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from .forms import SignUpForm
# Create your views here.

def home(request):
	#request.method you made in the html template page
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request,'Your information has been saved')
		return HttpResponseRedirect('/thank-you/')
		
	return render_to_response('signups.html', locals(), 
			context_instance=RequestContext(request))

def thankyou(request):
	#request.method you made in the html template page
	return render_to_response('thankyou.html', locals(), 
			context_instance=RequestContext(request))

def aboutus(request):
	return render_to_response('aboutus.html', locals(), 
		context_instance=RequestContext(request))

def more(request):
	return render_to_response('more.html', locals(), 
		context_instance=RequestContext(request))