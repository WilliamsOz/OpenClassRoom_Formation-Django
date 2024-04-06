from listings.models import Band, Listing
from django.shortcuts import render, get_object_or_404, redirect
from listings.form import ContactUsForm
from django.core.mail import send_mail

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

def email_sent(request):
	return render(request, 'email_sent.html')

def contact(request):
	if request.method == 'POST':
		# créer une instance de notre formulaire et le remplir avec les données POST
		form = ContactUsForm(request.POST)

		if form.is_valid():
			send_mail(
				subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
				message=form.cleaned_data['message'],
				from_email=form.cleaned_data['email'],
				recipient_list=['admin@merchex.xyz'],)
		return redirect('email-sent/')  # ajoutez cette instruction de retour  # ajoutez cette instruction de retour
	# si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
	# ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

	else:
	# ceci doit être une requête GET, donc créer un formulaire vide
		form = ContactUsForm()

	return render(request, 'listings/contact.html', {'form': form})