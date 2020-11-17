from django.shortcuts import render
from rest_framework import generics
from .models import Office, Service, Organization, SubscriptionType, UserInfo, Subscriber, TransferredSubscription, Officer, OrgMember
from .serializers import SubscriberSerializer, ServiceSerializer, OrganizationSerializer

class SubscriberView(generics.ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class SubscriberDetailView(generics.RetrieveAPIView): 
    queryset = Subscriber.objects.all() 
    serializer_class = SubscriberSerializer

class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class OrganizationView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
class OrganizationDetailView(generics.RetrieveAPIView): 
    queryset = Organization.objects.all() 
    serializer_class = OrganizationSerializer
