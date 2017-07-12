from django.conf.urls import url
from . import views


urlpatterns = [
	
	#index page
	url(r'^$', views.index, name='index'),

	#alternative home page
	url(r'^alternative/$', views.index_ajax, name='index_alt'),
    
    #VC Page
    # ex: /vc/?search_query=12/   8vc (e.g)
    url(r'^vc/$', views.vc_page, name='vc_page'),

    #Company Page
    #ex: /company/24 == uber (e.g.)
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_page, name='company_page'),

    url(r'^alternative/search/$', views.search , name='search')
]
