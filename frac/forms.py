from django.forms import ModelForm
from django import forms
from .models import *

class WellForm(forms.Form):
  name = forms.CharField(required=True)
  operator = forms.CharField(required=True)
  serviceco = forms.CharField(required=True)
  crew = forms.CharField(required=True)
  location = forms.CharField(required=True)
  directions = forms.CharField(required=True)

class SandForm(forms.Form):
  sand_name = forms.CharField(required=True)
  well_id = forms.CharField(required=True)
  facilities = forms.CharField(required=True)
  date_prefill = forms.CharField(required=True)
  po = forms.CharField(required=True)
  total_sand = forms.CharField(required=True)

class DriverForm(ModelForm):
  class Meta:
    model = Driver
    fields = '__all__'