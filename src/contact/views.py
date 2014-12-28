from django.shortcuts import render

# Create your views here.


def home(request):
	context = locals()
	template = "contact.html"
	return render(request, template, context)
