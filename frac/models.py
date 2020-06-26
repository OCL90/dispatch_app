from django.db import models

# Create your models here.


class Operator(models.Model):
  name = models.CharField(max_length=100, null=True)
  website = models.CharField(max_length=300, null=True, blank=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name

class ServiceCo(models.Model):
  name = models.CharField(max_length=100, null=True)
  website = models.CharField(max_length=300, null=True, blank=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name

class Crew(models.Model):
  name = models.CharField(max_length=100, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name

class LoadingFacility(models.Model):
  name = models.CharField(max_length=100, null=True)
  location = models.CharField(max_length=100, null=True)
  directions = models.TextField(max_length=2000, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name


class Well(models.Model):
  name = models.CharField(max_length=100, null=True)
  operator = models.ForeignKey(Operator, null=True, on_delete=models.CASCADE)
  serviceco = models.ForeignKey(ServiceCo, null=True, on_delete=models.CASCADE)
  crew = models.ForeignKey(Crew, null=True, on_delete=models.CASCADE)
  location = models.CharField(max_length=100, null=True)
  directions = models.TextField(max_length=2000, null=True)
  active = models.BooleanField(default=True, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name

class SandType(models.Model):
  sand_name = models.CharField(max_length=30, null=True)
  well = models.ForeignKey(Well, null=True, on_delete=models.CASCADE)
  date_prefill = models.CharField(max_length=30, null=True)
  po = models.CharField(max_length=30, null=True)
  loading_facility = models.ForeignKey(LoadingFacility, null=True, on_delete=models.CASCADE)
  total_sand = models.CharField(max_length=30, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.sand_name

class Truck(models.Model):
  truck_num = models.CharField(max_length=30, null=True)
  model = models.CharField(max_length=30, null=True)
  year = models.CharField(max_length=30, null=True)
  color = models.CharField(max_length=30, null=True)
  vin_num = models.CharField(max_length=30, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.truck_num

class Trailer(models.Model):
  trailer_num = models.CharField(max_length=30, null=True)
  model = models.CharField(max_length=30, null=True)
  year = models.CharField(max_length=30, null=True)
  vin_num = models.CharField(max_length=30, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  def __str__(self):
    return self.trailer_num

class Driver(models.Model):
  STATUS = (
    ('On Duty', 'On Duty'),
    ('Off Duty', 'Off Duty'),
    ('Down', 'Down'),
  )
  name = models.CharField(max_length=100, null=True)
  employer = models.CharField(max_length=30, null=True)
  status = models.CharField(max_length=100, null=True, choices=STATUS)
  truck = models.ForeignKey(Truck, null=True, blank=True, on_delete=models.CASCADE)
  trailer = models.ForeignKey(Trailer, null=True, blank=True, on_delete=models.CASCADE)
  available = models.BooleanField(default=True, null=True)
  date_created = models.DateField(auto_now_add=True, null=True)

  class Meta:
    unique_together = [['truck', 'trailer']]

  def __str__(self):
    return self.name 

class Order(models.Model):
  STATUS = (
    ('Dispatched', 'Dispatched'),
    ('Loaded', 'Loaded'),
    ('Complete', 'Complete'),
  )
  well = models.ForeignKey(Well, null=True, on_delete=models.CASCADE)
  sand = models.ForeignKey(SandType, null=True, on_delete=models.CASCADE)
  driver = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
  appt_time = models.CharField(max_length=50, null=True)
  request_weight = models.CharField(max_length=50, null=True)
  actual_weight = models.CharField(max_length=50, blank=True, null=True)
  load_date = models.CharField(max_length=50, null=True, blank=True)
  load_time_in = models.CharField(max_length=50, null=True, blank=True)
  load_time_out = models.CharField(max_length=50, null=True, blank=True)
  ticket_num = models.CharField(max_length=50, null=True, blank=True)
  bol_num = models.CharField(max_length=50, null=True, blank=True)
  loc_arrive_date = models.CharField(max_length=50, null=True, blank=True)
  loc_arrive_time = models.CharField(max_length=50, null=True, blank=True)
  loc_depart_date = models.CharField(max_length=50, null=True, blank=True)
  loc_depart_time = models.CharField(max_length=50, null=True, blank=True)
  status = models.CharField(max_length=100, default='Dispatched', null=True, choices=STATUS)
  date_created = models.DateField(auto_now_add=True, null=True)

