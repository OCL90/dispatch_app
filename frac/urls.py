from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sands/', views.sandsPage, name='sand-page'),
  path('operators/', views.operatorsPage, name='operators-page'),
  path('service_companies/', views.serviceCoPage, name='serviceco-page'),
  path('facilities/', views.facilitiesPage, name='facilities-page'),
  path('facilities/<str:pk>', views.facility, name='facility'),

  path('drivers/', views.driversPage, name='drivers-page'),
  path('create_driver/', views.createDriver, name='create_driver'),

  path('trucks_trailers_inventory/', views.trucksPage, name='trucks-page'),
  
  path('create_well/', views.createWell, name='create_well'),
  path('well/<str:pk>/', views.well, name='well'),
  path('well/<str:pk>/update/', views.updateWell, name='update_well'),
  path('well/<str:pk>/delete/', views.deleteWell, name='delete_well'),

  path('c_sand/<str:pk>/', views.cSandType, name='c_sand'),

  path('sand/<str:pk1>/', views.sand_type, name='sand'),


]