from django import forms
from django.forms import ModelForm
from .models import *

class dproduct(forms.ModelForm):
	class Meta:
		model=product
		fields='__all__'
		widgets={
			'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
			'owner_email': forms.TextInput(attrs={'class': 'form-control'}),
			'noofbed': forms.TextInput(attrs={'class': 'form-control'}),
			'desc': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'postelcode': forms.TextInput(attrs={'class': 'form-control'}),

		}

class qform(forms.ModelForm):
		class Meta:
			model=qfield
			fields="__all__"
			widgets={
				'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
				'owner_email': forms.TextInput(attrs={'class': 'form-control'}),
				'your_name': forms.TextInput(attrs={'class': 'form-control'}),
				'your_city': forms.TextInput(attrs={'class': 'form-control'}),
				'your_email': forms.TextInput(attrs={'class': 'form-control'}),
			}
			