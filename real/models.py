from django.db import models

# Create your models here.

class product(models.Model):
	owner_name=models.CharField(max_length=50)
	owner_email=models.EmailField()
	noofbed=models.IntegerField()
	decs=models.TextField()
	price=models.IntegerField()
	city=models.CharField(max_length=50)
	postelcode=models.IntegerField()
	category=(('Villa','Villa'),
				('Banglov','Banglov'),
				('Land','Land'),
				('Apartment','Apartment'),
				('Office','Office'),
				('Warehouse','Warehouse')
		)
	Category=models.CharField(max_length=50,choices=category)
	img=models.ImageField()


	def __str__(self):
		return self.Category


class qfield(models.Model):
	owner_name=models.CharField(max_length=50)
	owner_email=models.EmailField()
	your_name=models.CharField(max_length=50)
	your_city=models.CharField(max_length=50)
	your_email=models.EmailField()

	def __str__(self):
		return self.your_name