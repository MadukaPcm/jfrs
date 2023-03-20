from django.urls import path
from reportdata import views

#paths for account app.
urlpatterns = [
    path('', views.OpenfileView, name='Openfile_url'),
    path('fileList/', views.FileListView, name='fileList_url'),
    
    path('Loafum/', views.LoafumView, name='Loafum_url'),
    path('createlofum/',views.CreateloafunView, name='createlofum_url'),
    path('atl/<str:pk>', views.UpdateatlView, name='atl_url'),
    path('sfd/<str:pk>', views.UpdatesfdView, name='sfd_url'),
    path('efd/<str:pk>', views.UpdateefdView, name='efd_url'),
    path('pdd/', views.PddView, name='pdd_url'),
    
    path('VesselList/', views.VesselListView, name='VesselList_url'),
    path('createvessel/', views.CreateVesselbView, name='createvesselb_url'),
    path('loadvessel/', views.LoadVesselView, name='loadvessel_url'),
    path('adp/<str:pk>', views.UpdateadpView, name='adp_url'),
    path('ada/<str:pk>', views.UpdateadaView, name='ada_url'),
    path('rd/<str:pk>', views.UpdaterdView, name='rd_url'),
    path('report/', views.ReportView, name='report_url'),
]