from django.http import HttpResponse
from listings.models import Band
# from listings.models import Title
	# titles = Title.objects.all()
from django.shortcuts import render

def	hello(request):
	bands = Band.objects.all()
	return render(request, 'listings/hello.html', {'bands': bands})

def	about(request):
	return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def	listings(request):
	return HttpResponse('<h1>COUCOU</h1>')

def	contact(request):
	return HttpResponse('<h1>CNS</h1>')