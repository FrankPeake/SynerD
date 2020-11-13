from django.db import models


class Office(models.Model):
    OfficeCode = models.CharField(primary_key=True, max_length=24)
    OfficeName = models.CharField(max_length=24)
    Attribution = models.CharField(max_length=24)

    def __str__(self):
        return self.OfficeCode

class Service(models.Model):
    ServiceCode = models.CharField(primary_key=True, max_length=24)
    ServiceName = models.CharField(max_length=24)
    Description = models.CharField(max_length=100)
    premium = models.DecimalField(max_digits=30, decimal_places=2)
    allocation = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.ServiceCode

class Organization(models.Model):
    OrgCode = models.CharField(primary_key=True, max_length=24)
    OrgName = models.CharField(max_length=24)
    Description = models.CharField(max_length=100)
    DateJoined = models.DateField()
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100)
    City = models.CharField(max_length=24)
    State = models.CharField(max_length=24)
    Zipcode = models.CharField(max_length=10)
    Phone = models.CharField(max_length=24)

    def __str__(self):
        return self.OrgCode

class SubscriptionType(models.Model):
    SubTypeCode = models.CharField(primary_key=True, max_length=24)
    SubTypeName = models.CharField(max_length=24)

    def __str__(self):
        return self.SubTypeCode

class UserInfo(models.Model):
    Username = models.CharField(primary_key=True, max_length=24)
    Password = models.CharField(max_length=24)
    FirstName = models.CharField(max_length=24)
    MiddleName = models.CharField(max_length=24)
    LastName = models.CharField(max_length=24)
    Gender = models.CharField(max_length=24)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=24)
    State = models.CharField(max_length=24)
    ZipCiode = models.CharField(max_length=24)
    Email = models.CharField(max_length=24)
    CellPhone = models.CharField(max_length=24)
    Citizenship = models.CharField(max_length=24)
    DateOfBirth = models.DateField()
    Organization = models.CharField(max_length=24)
    
    def __str__(self):
        return self.Username

class Subscriber(models.Model):
    SubscriberID = models.CharField(primary_key=True, max_length=24)
    ServiceCode = models.ForeignKey(Service, on_delete=models.CASCADE)
    SubRequestDate = models.DateField()
    SubStartDate = models.DateField()
    SubEndDate = models.DateField()
    Cancellation = models.CharField(max_length=24)
    SubTypeCode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    Username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#	beneficiaryID = models.ForeignKey(OrgMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.SubscriberID

class TransferredSubscription(models.Model):
    TransferID = models.CharField(primary_key=True, max_length=24)
    TransferTo = models.CharField(max_length=24) 
    RequestDate = models.DateField() 
    TransferDate = models.DateField() 
    SubscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    def __str__(self):
        return self.TransferID

class Officer(models.Model):
    SubscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    OfficeCode = models.ForeignKey(Office, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __str__(self):
        return self.SubscriberID

class OrgMember(models.Model):
    OrgCode = models.ForeignKey(Organization, on_delete=models.CASCADE)
    SubscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    MemberStartDate = models.DateField()
    MemberEndDate = models.DateField()
    NativeCountry = models.CharField(max_length=24)
    Citizenship = models.CharField(max_length=24)
    isDelegate = models.CharField(max_length=24)

    def __str__(self):
        return self.OrgCode