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
			context = {}

			#gets item from database			
			VC_info = VC_data.objects.all().filter(vc_name='%s' %query)
			if(VC_info.exists()):				
				#Getting all the VCs investments			
				vc_id = VC_info.values('vid').get()['vid']				
				Investments = VC_Company.objects.filter(vid=vc_id).values('company_name','cid')				
				# print("-------- INVESTMENTS --------", Investments)

				### Getting information of portfolio companies ###				
				for comp in Investments:
					temp = Companies.objects.filter(cid=comp['cid']).values().get()
					#adding all the company infos into Investments dictionary
					for item in temp:
						comp[item] = temp[item]

				context = {'VC_info': VC_info, 'Investments': Investments}			
				return render(request, 'vcplatform/vcdashboard.html', context)
			else:
				raise Http404("VC does not exist")
			#print(context)	
		except VC_data.DoesNotExist:
		    raise Http404("VC does not exist")
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