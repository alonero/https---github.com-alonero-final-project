from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# Admin SuperUser Event Form
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description', 'category')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Job location',
			'manager': 'Manager',
			'attendees': 'Employees',
			'description': '',
			'category': 'Category',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Date'}),
			'venue': forms.Select(attrs={'class':'form-select'}),
			'manager': forms.Select(attrs={'class':'form-select'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'category': forms.Select(attrs={'class':'form-select'}),
		}

# User Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'attendees', 'description', 'category')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Job location',
			'attendees': 'Employees',
			'description': '',
			'category': 'Category',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Date'}),
			'venue': forms.Select(attrs={'class':'form-select'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'category': forms.Select(attrs={'class':'form-select'}),
		}

# Create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', 'venue_image')
		labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': '',
			'venue_image': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
		}
