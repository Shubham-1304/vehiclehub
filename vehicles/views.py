from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Vehicle

class VehicleList(ListView):
    model=Vehicle
    context_object_name='vehicles'


class VehicleDetail(DetailView):
    model=Vehicle
    context_object_name='vehicle'

class VehicleCreate(CreateView):
    model=Vehicle
    fields='__all__'
    success_url=reverse_lazy('vehicles')

class VehicleUpdate(UpdateView):
    model=Vehicle
    fields='__all__'
    success_url=reverse_lazy('vehicles')

    def post(self, request, *args, **kwargs):
        print("hello")
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
class VehicleDelete(DeleteView):
    model=Vehicle
    context_object_name='vehicle'
    success_url=reverse_lazy('vehicles')