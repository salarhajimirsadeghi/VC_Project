from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import VC_data, Companies, VC_Company
# Create your views here.


def index(request):
	count_vc = VC_data.objects.count()
	count_company = Companies.objects.count()
	context = {'count_vc': count_vc, 'count_company': count_company}
	return render(request, 'vcplatform/index_cover.html')


#Retrieves the description of vcs given the vc_id
def vc_page(request, vc_id):	
	
	try:
		VC_description = VC_data.objects.values('description').filter(vid='%s' %vc_id)
		context = {'description': VC_description}		
		# print(context)	
	except VC_data.DoesNotExist:
	    raise Http404("VC ID does not exist")
	return render(request, 'vcplatform/vc_home.html', context)


#Retrieves the description of companies given the compnay_id
def company_page(request, company_id):

	try:
		Company_Description = Companies.objects.values('description').filter(cid='%s' %company_id)
		context = {'description': Company_Description}	
	except Companies.DoesNotExist:
	    raise Http404("VC ID does not exist")

	return render(request, 'vcplatform/company_home.html', context)