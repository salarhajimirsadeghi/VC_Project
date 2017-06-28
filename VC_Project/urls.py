"""VC_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from vcplatform import views
from vcplatform import models


urlpatterns = [
    
    #index page
    url(r'^$', views.index, name='index'),
    
    #VC Page --- ex: /vc/12/ == 8vc (e.g)
    url(r'^vc/(?P<vc_id>[0-9]+)/$', views.vc_page, name='vc_page'),

    #Company Page ---- ex: /company/24 == uber (e.g.)
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_page, name='company_page'),
]