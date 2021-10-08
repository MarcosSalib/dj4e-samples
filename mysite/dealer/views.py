from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Doctor, Patient, Prescription, Pharmacy, Laboratory

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        patients_count = Patient.objects.all().count()
        ctx = {'Total number of patients: ': patients_count}
        return render(request, 'dealer/..', ctx)
