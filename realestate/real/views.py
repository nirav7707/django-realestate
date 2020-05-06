from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
# Create your views here.
def main(request):
	eget=product.objects.all()
	myfilter=property(request.GET,queryset=eget)
	eget=myfilter.qs
	context={'get':eget ,'myfilter':myfilter}
	return render(request,'home.html',context)


def get_value(request,i_id):
	
	get=get_object_or_404(product,pk=i_id)
	makequery=qform()
	if request.method=='POST':
		makequery=qform(request.POST)
		if makequery.is_valid():
			makequery.save()
			return render('/')
	context={'get':get,'makequery':makequery}
	return render(request,'show.html',context)


def create(request):
	form=dproduct()
	if request.method=='POST':
		form=dproduct(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=dproduct()



	context={'form':form}
	return render(request,'form.html',context)

def success(request):
	return HttpResponse('successfully uploaded')

