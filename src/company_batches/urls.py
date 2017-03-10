from django.conf.urls import url, include

from .views import (
    CompanyBatchListView,
    CompanyBatchCreateView,
    ResumeCreateView,
    CoverLetterCreateView
)

app_name = 'company_batches'

urlpatterns = [
    url(r'^$', CompanyBatchListView.as_view(), name='list'),
    url(r'^create/$', CompanyBatchCreateView.as_view(), name='create'),
    url(r'resume/$', ResumeCreateView.as_view(), name='resume' ),
    url(r'cover/$', CoverLetterCreateView.as_view(), name='cover' ),

]