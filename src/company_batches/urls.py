from django.conf.urls import url

from .views import (
    CompanyBatchListView,
)

urlpatterns = [
    url(r'^$', CompanyBatchListView.as_view(), name='list')
]