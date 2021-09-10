from django.conf.urls import url,include
from rest_framework import routers
from .views import *


urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^sf_login/$', SalesForceAuth.as_view()),
    url(r'^get_data/$', GetData.as_view()),

]