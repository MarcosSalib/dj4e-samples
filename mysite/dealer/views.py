from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Clinic, Patient, Prescription, Pharmacy, Laboratory, InsuranceCompany

# Create your views here.
# TODO arranging MainView


class MainView(LoginRequiredMixin, View):
    # home screen for the doctor
    pass

class PatientView(LoginRequiredMixin, View):
    def get(self, request):
        patient_history = Patient.objects.get(id=1)
        patients_count = Patient.objects.all().count()
        ctx = {
            'Patient Medical History: ': patient_history,
            'Total number of patients: ': patients_count,
            }
        return render(request, 'dealer/..', ctx)


class InsuranceCompanyView(LoginRequiredMixin, View):
    pass


class ClinicView(LoginRequiredMixin, View):
    pass


class CalendarView(LoginRequiredMixin, View):
    pass