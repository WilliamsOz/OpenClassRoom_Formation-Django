from listings.models import Band, Listing
from django.shortcuts import render, get_object_or_404

def	band_list(request):
	band = Band.objects.all()
	return render(request, 'band_list.html', {'bands': band})

def band_detail(request, band_id):  # notez le paramètre id supplémentaire
	band = get_object_or_404(Band, pk=band_id)
	return render(request, 'listings/band_detail.html', {'band': band}) # nous passons l'id au modèle

def	listing_list(request):
	listing = Listing.objects.all()
	return render(request, 'listings_list.html', {'listings': listing})

def listing_detail(request, listing_id):
	listing = get_object_or_404(Listing, pk=listing_id)
	return render(request, 'listings_detail.html', {'listing': listing})

def	about(request):
	return render(request, 'about.html')

def	contact(request):
	return render(request, 'contact.html')

def handler404(request, exception):
	return render(request, '404.html', status=404)