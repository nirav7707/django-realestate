from django import forms
from django.forms import ModelForm
from .models import *

class dproduct(forms.ModelForm):
	class Meta:
		model=product
		fields='__all__'

class qform(forms.ModelForm):
	class Meta:
		model=qfield
		fields='__all__'