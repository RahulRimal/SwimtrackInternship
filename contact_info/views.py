from django.shortcuts import render
from contact_info.models import ContactInfo
from datetime import datetime
import requests

# Create your views here.

def contact_info(request):
	response = requests.get('https://ipinfo.io/')
	data = response.json()
	city = data['city']
	loc_coordinate = data['loc']
	if request.method == 'POST':
		name = request.POST.get('name')

		new_message = ContactInfo(name = name, submitted_time = datetime.utcnow(), location = loc_coordinate, city = city)
		new_message.save()

	return render(request, 'contacts.html')