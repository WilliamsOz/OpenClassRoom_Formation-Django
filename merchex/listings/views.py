from listings.models import Band, Title
from django.shortcuts import render

def	hello(request):
	bands = Band.objects.all()
	return render(request, 'hello.html', {'bands': bands})

def	listings(request):
	titles = Title.objects.all()
	return render(request, 'listings.html', {'titles': titles})

def	about(request):
	return render(request, 'about.html')

def	contact(request):
	return render(request, 'contact.html')