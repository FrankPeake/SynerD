from django.contrib import admin
from .models import Office, Officer, Organization, OrgMember, Subscriber

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['OfficeCode', 'OfficeName', 'Attribution']
    search_fields = ('OfficeCode', 'OfficeName')
    list_filter = ()

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ['SubscriberID', 'OfficeCode', 'StartDate', 'EndDate']
    search_fields = ('SubscriberID', 'OfficeCode')
    list_filter = ('StartDate', )

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['OrgCode', 'OrgName', 'Description', 'DateJoined', 'Address1', 'Address2', 'City', 'State', 'Zipcode', 'Phone']
    search_fields = ('OrgCode', 'OrgName')
    list_filter = ('State', 'DateJoined')
    fieldsets = (
        (None, {
            'fields': ('OrgCode', 'OrgName', 'Description', 'DateJoined', 'Phone')
        }),
        ('Address', {
            'fields': ('Address1', 'Address2', 'City', 'State', 'Zipcode')
        })
    )

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ['OrgCode', 'SubscriberID', 'MemberStartDate', 'MemberEndDate', 'NativeCountry', 'Citizenship', 'isDelegate']
    search_fields = ('OrgCode', 'SubscriberID')
    list_filter = ('NativeCountry', 'MemberStartDate' )

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['SubscriberID', 'ServiceCode', 'SubRequestDate', 'SubStartDate', 'SubEndDate', 'Cancellation', 'SubTypeCode', 'Username']
    search_fields = ('SubscriberID', 'ServiceCode', 'Username')
    list_filter = ('SubRequestDate', )

# Register your models here.
