from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sands/', views.sandsPage, name='sand-page'),

  path('operators/', views.operatorsPage, name='operators-page'),
  path('create_operator/', views.createOperator, name='create_operator'),
  path('operator/<str:pk>', views.operator, name='operator'),
  path('operator/<str:pk>/update/', views.updateOperator, name='update_operator'),
  path('operator/<str:pk>/delete/', views.deleteOperator, name='delete_operator'),

  path('service_companies/', views.serviceCoPage, name='serviceco-page'),
  path('serviceco/<str:pk>', views.serviceco, name='serviceco'),

  path('facilities/', views.facilitiesPage, name='facilities-page'),
  path('create_facility/', views.createFacility, name='create_facility'),
  path('facility/<str:pk>', views.facility, name='facility'),
  path('facility/<str:pk>/update/', views.updateFacility, name='update_facility'),
  path('facility/<str:pk>/delete/', views.deleteFacility, name='delete_facility'),
  

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