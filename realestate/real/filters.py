import django_filters
from .models import *


class property(django_filters.FilterSet):
	class Meta:
		model =product
		fields=['price','city','postelcode','Category']
