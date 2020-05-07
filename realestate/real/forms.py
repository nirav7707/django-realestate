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

class qform(forms.Form):
		owner_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="owner_nmae")
		owner_email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label="owner_email")
		your_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="your_nmae")
		your_email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label="r_email")