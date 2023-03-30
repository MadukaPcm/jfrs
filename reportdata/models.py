from django.db import models
from uaa.models import User
import uuid
from datetime import date,timedelta


#  @property
#     def IsDueForM(self):
#         return (date.today()-self.lastMaintained).days >= (self.mtl-3)
    
# Create your models here.
class VesselBooking(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    bookingDate = models.DateField()
    eVesselName = models.CharField(max_length=100,blank=True,null=True)
    aVesselName = models.CharField(max_length=100,blank=True,null=True)
    carrierBookingRef = models.CharField(max_length=100,blank=True,null=True)
    mbol = models.CharField(max_length=100,blank=True,null=True) #master bill of lading
    
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_vesselBooking", null=True, blank=True)
    updatedBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_vesselBookig", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.carrierBookingRef)
    
    
class Openf(models.Model):  
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    user = models.ForeignKey(User, related_name='user_opennf', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    itemNo = models.PositiveIntegerField(unique=True)
    batchNo = models.PositiveIntegerField()
    mopi = models.CharField(max_length=30,blank=True,null=True)
    contqnty = models.PositiveIntegerField()
    type = models.CharField(max_length=20,blank=True,null=True)
    transferPoNo = models.PositiveIntegerField()
    freightBookingNo = models.PositiveIntegerField()
    carrierName = models.CharField(max_length=100,blank=True,null=True)
    vesselBooking = models.OneToOneField(VesselBooking, related_name='vesselBooking_openf', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    etd = models.DateField() #expected time of departure
    eta = models.DateField() #exepected time of arrival
    etaNo = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_openf", null=True, blank=True)
    updatedBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_openff", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isDone = models.BooleanField(default=False)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.itemNo)
    

class Loafum(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    openf = models.OneToOneField(Openf, related_name='openf_loafum', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    lfuser = models.ForeignKey(User, related_name='loafm_user', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    eloadingDate = models.DateField() 
    aloadingDate = models.DateField() 
    aloadingDateNo = models.IntegerField(default=0)
    fumigationStartDate = models.DateField()
    fumigationStartDateNo = models.IntegerField(default=0)
    fumigationEndDate = models.DateField()
    fumigationEndDateNo = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_loafum", null=True, blank=True)
    updatedBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_loafumm", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isDone = models.BooleanField(default=False)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
class loaVessel(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    loafum = models.OneToOneField(Loafum, related_name='loafm_loavessel', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    lvuser= models.ForeignKey(User, related_name='loavs_user', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    portDeliveryDate = models.DateField()
    adateDeparture = models.DateField()
    adateDepartureNo = models.IntegerField(default=0)
    adateArrival = models.DateField()
    adateArrivalNo = models.IntegerField(default=0)
    siReceiveDate = models.DateField()
    siReceiveDateNo = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_loavesel", null=True, blank=True)
    updatedBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_loavessel", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isDone = models.BooleanField(default=False)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
