from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *

# Create your views here.
def home(request):
  wells = Well.objects.all()

  active_wells = wells.filter(active=True).count()
  inactive_wells = wells.filter(active=False).count()

  operators = Operator.objects.all()
  servicecos = ServiceCo.objects.all()
  crews = Crew.objects.all()

  context = {'wells': wells, 'operators': operators, 'servicecos':servicecos , 'crews': crews, 'active_wells': active_wells, 'inactive_wells': inactive_wells}
  return render(request, 'frac/dashboard.html', context)

def well(request, pk):
  facilities = LoadingFacility.objects.all()
  
  well = Well.objects.get(id=pk)
  sands = well.sandtype_set.all()

  drivers = Driver.objects.all()
  available_drivers = drivers.filter(available = True)

  orders = well.order_set.all()
  dispatched = orders.filter(status='Dispatched').all()
  loaded = orders.filter(status='Loaded').all()
  complete = orders.filter(status='Complete').all()

  form = WellsForm()
  form = WellsForm(instance=well)

  context = {'well': well, 'sands': sands, 'available_drivers': available_drivers, 'dispatched': dispatched, 'loaded': loaded, 'complete': complete, 'facilities': facilities, 'form': form}
  return render(request, 'frac/well_info.html', context)

def sand_type(request, pk1):
  context = {}
  return render(request, 'frac/sand_orders.html', context)

def createWell(request):
  form = WellForm()
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = WellForm(request.POST)
    print('Printing FORM: ', form)
    if form.is_valid():
      name = form.cleaned_data['name']
      operator = form.cleaned_data['operator']
      serviceco = form.cleaned_data['serviceco']
      crew = form.cleaned_data['crew']
      location = form.cleaned_data['location']
      directions = form.cleaned_data['directions']
      f = Well(name=name, operator_id=operator, serviceco_id=serviceco, crew_id=crew, location=location, directions=directions)
      f.save()
      return redirect('/')
    else:
      print("error")
  
  context = {}
  return render(request, 'frac/well_form.html', context)

def updateWell(request, pk):
  well = Well.objects.get(id=pk)
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = WellsForm(request.POST, instance=well)
    if form.is_valid():
      form.save()
      return redirect('well', pk=well.id)
    else:
      print("error")

  context = {}
  return render(request, 'frac/well_update_form.html', context)

def deleteWell(request, pk):
  well = Well.objects.get(id=pk)

  if request.method == 'POST':
    well.delete()
    return redirect('/')

  context = {}
  return render(request, 'frac/well_delete_form.html', context)

def cSandType(request,pk):
  well = Well.objects.get(id=pk)
  form = SandForm()
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = SandForm(request.POST)
    print('Printing FORM: ', form)
    if form.is_valid():
      sand_name = form.cleaned_data['sand_name']
      well_id = form.cleaned_data['well_id']
      loading_facility_id = form.cleaned_data['facilities']
      date_prefill = form.cleaned_data['date_prefill']
      po = form.cleaned_data['po']
      total_sand = form.cleaned_data['total_sand']
      f = SandType(sand_name=sand_name, well_id=well_id, loading_facility_id=loading_facility_id, date_prefill=date_prefill, po=po, total_sand=total_sand)
      f.save()
      return redirect('well', pk=well.id)
    else:
      print("error")
  
  context = {}
  return render(request, 'frac/sand_form.html', context)

def sandsPage(request):
  context = {}
  return render(request, 'frac/sands_page.html', context)

def operatorsPage(request):
  operators = Operator.objects.all()
  form = OperatorForm()
  

  context = {'form': form, 'operators': operators}
  return render(request, 'frac/operators_page.html', context)

def createOperator(request):
  
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = OperatorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/operators')
  else:
      print("error")

  context = {'form': form}
  return render(request, 'frac/operator_form.html', context)

def updateOperator(request, pk):
  operator = Operator.objects.get(id=pk)
  form = OperatorForm(instance=operator)
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = OperatorForm(request.POST, instance=operator)
    if form.is_valid():
      form.save()
      return redirect('/operators')
    else:
      print("error")

  context = {'form': form, 'operator': operator}
  return render(request, 'frac/operator_update_form.html', context)


def serviceCoPage(request):
  context = {}
  return render(request, 'frac/serviceco_page.html', context)

def facilitiesPage(request):
  facilities = LoadingFacility.objects.all()
  context = {'facilities': facilities}
  return render(request, 'frac/facilities_page.html', context)

def facility(request, pk):
  facility = LoadingFacility.objects.get(id=pk)

  context = {'facility': facility}
  return render(request, 'frac/facility_info.html', context)

def driversPage(request):
  drivers = Driver.objects.all()

  total_drivers = drivers.count()
  onduty = drivers.filter(status = 'On Duty').count()
  offduty = drivers.filter(status = 'Off Duty').count()
  down = drivers.filter(status = 'Down').count()

  context = {'drivers': drivers, 'onduty': onduty, 'offduty': offduty, 'down': down, 'total_drivers': total_drivers}
  return render(request, 'frac/drivers_page.html', context)

def createDriver(request):
  form = DriverForm()
  if request.method == 'POST':
    print('Printing POST: ', request.POST)
    form = DriverForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/drivers')

  context = {'form': form}
  return render(request, 'frac/driver_form.html', context)

def trucksPage(request):
  trucks = Truck.objects.all()
  trailers = Trailer.objects.all()

  context = {'trucks': trucks, 'trailers': trailers}
  return render(request, 'frac/trucks_page.html', context)