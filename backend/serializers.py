from rest_framework import serializers
from .models import Office, Service, Organization, SubscriptionType, UserInfo, Subscriber, TransferredSubscription, Officer, OrgMember

class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'