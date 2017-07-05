from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import VC_data, Companies, VC_Company
# Create your views here.


def index(request):
	count_vc = VC_data.objects.count()
	count_company = Companies.objects.count()
	context = {'count_vc': count_vc, 'count_company': count_company}
	return render(request, 'vcplatform/index.html')


#Retrieves the description of vcs given the vc_id
def vc_page(request):			

	#grabs the search query that was stored from our submit button
	if (request.method == 'GET'):
		query = request.GET.get('search_query', None)
		try:
			#gets item from database
			VC_info = VC_data.objects.all().filter(vid='%s' %query)		
			context = {'VC_info': VC_info}	
			# print(context)	
		except VC_data.DoesNotExist:
		    raise Http404("VC ID does not exist")
		return render(request, 'vcplatform/vcdashboard.html', context)
	
	else:
		raise Http404("NOT A GET METHOD")

#Retrieves the description of companies given the compnay_id
def company_page(request, company_id):

	try:
		Company_Description = Companies.objects.values('description').filter(cid='%s' %company_id)
		context = {'description': Company_Description}	
	except Companies.DoesNotExist:
	    raise Http404("VC ID does not exist")

	return render(request, 'vcplatform/company_home.html', context)