from django.http import HttpResponse
from listings.models import Band
from listings.models import Title
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
	return render(request, 'about.html')