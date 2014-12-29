from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm
# Create your views here.





def home(request):
	title = "Contact"
	form = ContactForm(request.POST or None)
	context = {
			"title": title,
			"form": form,
		}
	confirm_message = None

	if form.is_valid():
		comment = form.cleaned_data['comment']
		name = form.cleaned_data['name']
		sbj = "Message from Seven.com"
		msg = "%s %s" %(comment, name)
		frm = " "
		to_us = [settings.EMAIL_HOST_USER]
		print sbj, msg, frm, to_us
		send_mail(sbj, msg, frm, to_us, fail_silently=True)
		title = "Thank You"
		confirm_message = """
		Thank you for your message. We have recieved it and we are reviewing it.
		"""

		context = {
			"title": title,
			"form": form,
			"confirm_message": confirm_message
		}

		form = None
		
	template = "contact.html"
	return render(request, template, context)
