from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import *

urlpatterns = [
    url(r'^risk_type/(?P<pk>[0-9]+)/$', RiskTypeDetail.as_view()),
    url(r'^risk_type/$', RiskTypeList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
