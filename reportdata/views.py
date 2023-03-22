from django.shortcuts import render,HttpResponse,redirect
from reportdata.models import Openf,Loafum,VesselBooking,loaVessel
from django.contrib import messages
from uaa.models import User

# Create your views here.
def OpenfileView(request):
    try:
        loggedinInstance = request.user
        if request.method == "POST":
            userId = request.POST.get('userId')
            ItemNo = request.POST.get('ItemNo')
            BatchNo = request.POST.get('BatchNo')
            Mopi = request.POST.get('Mopi')
            Contqnty = request.POST.get('Contqnty')
            Type = request.POST.get('Type')
            TransferPoNo = request.POST.get('TransferPoNo')
            FreightBookingNo = request.POST.get('FreightBookingNo')
            CarrierName = request.POST.get('CarrierName')
            VesselBookingId = request.POST.get('VesselBookingId')
            Etd = request.POST.get('Etd')
            Eta = request.POST.get('Eta')
            
            asloggeginInstance = User.objects.get(id=userId)
            if loggedinInstance == asloggeginInstance:
                messages.info(request,"can't create your own file")
                return redirect('uaaUserList_url')
            
            if Openf.objects.filter(vesselBooking__id=VesselBookingId).first():
                messages.info(request,'The carrier book reference already exist, create new one')
                return redirect('uaaUserList_url')
            
            if Openf.objects.filter(itemNo=ItemNo).first():
                messages.info(request,'The item already exist, create new one')
                return redirect('uaaUserList_url')
        
            Openf.objects.create(
                user_id=userId,
                itemNo=ItemNo,
                batchNo=BatchNo,
                mopi=Mopi,
                contqnty=Contqnty,
                type=Type,
                transferPoNo=TransferPoNo,
                freightBookingNo=FreightBookingNo,
                carrierName=CarrierName,
                vesselBooking_id=VesselBookingId,
                etd=Etd,
                eta=Eta,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id
            )
            # Inventory.tags.set(tags)
            messages.success(request, 'file created succesfully')
            return redirect('fileList_url')
        
    except:
        return render(None, 'uaa/error500.html')

def FileListView(request):
    fileInstance = Openf.objects.filter(status=True)
    
    context = {"fileInstance":fileInstance}
    return render(request, 'reportdata/fileList.html', context)

def LoafumView(request):
    loafumInstance = Loafum.objects.filter(status=True)
        
    context = {"loafumInstance":loafumInstance}
    return render(request, 'reportdata/loafum.html', context)

def CreateloafunView(request):
    
    try:
        if request.method == "POST":
            fileId = request.POST.get('fileId')
            EloadingDate = request.POST.get('EloadingDate')
            
            if Loafum.objects.filter(openf__id=fileId).first():
                messages.info(request,'It already exist')
                return redirect('fileList_url')
        
            Loafum.objects.create(
                openf_id=fileId,
                eloadingDate=EloadingDate,
                aloadingDate=EloadingDate,
                fumigationStartDate=EloadingDate,
                fumigationEndDate=EloadingDate,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'etl assigned succesfully')
            return redirect('fileList_url')
        
    except:
        return render(None, 'uaa/error500.html')
    
def UpdateatlView(request,pk):
    
    try:
        if request.method == "POST":
            AloadingDate = request.POST.get('AloadingDate')
            
            Loafum.objects.filter(id=pk).update(
                aloadingDate=AloadingDate,
                aloadingDateNo=1,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'changed a-loadingDate')
            return redirect('Loafum_url')
    except:
        return render(None, 'uaa/error500.html')

def UpdatesfdView(request, pk):
    
    try:
        if request.method == "POST":
            FumigationStartDate = request.POST.get('FumigationStartDate')
            
            Loafum.objects.filter(id=pk).update(
                aloadingDate=FumigationStartDate,
                fumigationStartDateNo=2,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'changed a-loadingDate')
            return redirect('Loafum_url')
    
    except:
        return render(None, 'uaa/error500.html')

def UpdateefdView(request, pk):
    
    try:
        if request.method == "POST":
            FumigationEndDate = request.POST.get('FumigationEndDate')
            
            Loafum.objects.filter(id=pk).update(
                fumigationEndDate=FumigationEndDate,
                fumigationEndDateNo=3,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'updated end-fum-Date')
            return redirect('Loafum_url')
    
    except:
        return render(None, 'uaa/error500.html')
    
def PddView(request):
    try:
        if request.method == "POST":
            loafumId = request.POST.get('loafumId')
            portDeliveryDate = request.POST.get('portDeliveryDate')
            
            if loaVessel.objects.filter(loafum__id=loafumId).first():
                messages.info(request,'already exist')
                return redirect('Loafum_url')
            
            loaVessel.objects.create(
                loafum_id=loafumId,
                portDeliveryDate=portDeliveryDate,
                adateDeparture=portDeliveryDate,
                adateArrival=portDeliveryDate,
                siReceiveDate=portDeliveryDate,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'port d-date updated')
            return redirect('Loafum_url')
    
    except:
        return render(None, 'uaa/error500.html')
    
    
def VesselListView(request):
    vesselInstance = VesselBooking.objects.all()
    
    context = {"vesselInstance":vesselInstance}
    return render(request, 'reportdata/vesselList.html', context)

def CreateVesselbView(request):
    
    try:
        if request.method == "POST":
            bookingDate = request.POST.get('bookingDate')
            eVesselName = request.POST.get('eVesselName')
            aVesselName = request.POST.get('aVesselName')
            carrierBookingRef = request.POST.get('carrierBookingRef')
            mbol = request.POST.get('mbol')
        
            VesselBooking.objects.create(
                bookingDate=bookingDate,
                eVesselName=eVesselName,
                aVesselName=aVesselName,
                carrierBookingRef=carrierBookingRef,
                mbol=mbol,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'created succesfully')
            return redirect('VesselList_url')
    
    except:
        return render(None, 'uaa/error500.html')

def LoadVesselView(request):
    
    ldvsInstance = loaVessel.objects.filter(status=True)
    
    context = {"ldvsInstance":ldvsInstance}
    return render(request, 'reportdata/loadvessel.html', context)

def UpdateadpView(request, pk):
    
    try:
        if request.method == "POST":
            AdateDeparture = request.POST.get('AdateDeparture')
            
            loaVessel.objects.filter(id=pk).update(
                adateDeparture=AdateDeparture,
                adateDepartureNo=1,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'updated date-departure')
            return redirect('loadvessel_url')
    
    except:
        return render(None, 'uaa/error500.html')
    
def UpdateadaView(request, pk):
    
    try:
        if request.method == "POST":
            AdateArrival = request.POST.get('AdateArrival')
            
            loaVessel.objects.filter(id=pk).update(
                adateArrival=AdateArrival,
                adateArrivalNo=2,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'updated a-data-arrival')
            return redirect('loadvessel_url')
    
    except:
        return render(None, 'uaa/error500.html')
    
def UpdaterdView(request, pk):
    
    try:
        if request.method == "POST":
            SiReceiveDate = request.POST.get('SiReceiveDate')
            
            loaVessel.objects.filter(id=pk).update(
                siReceiveDate=SiReceiveDate,
                siReceiveDateNo=3,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'received by customer')
            return redirect('loadvessel_url')
    
    except:
        return render(None, 'uaa/error500.html')
    

def ReportView(request):
    
    context = {}
    return render(request, 'reportdata/reportpage.html', context)
