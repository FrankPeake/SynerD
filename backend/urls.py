from django.urls import path
from . import views


urlpatterns = [ 
    path('subscribers/', views.SubscriberView.as_view(), name='subscriber_list'), 
    path('subscribers/<pk>/', views.SubscriberDetailView.as_view(), name='subscriber_detail'),
    path('services/', views.ServiceView.as_view(), name='service_list'), 
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('organizations/', views.OrganizationView.as_view(), name='organization_list'), 
    path('organizations/<pk>/', views.OrganizationDetailView.as_view(), name='organization_detail'),
]
