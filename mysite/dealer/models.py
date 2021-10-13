from django.db import models
from django.db.models.fields import related

# Create your models here.


class GeneralUser(models.Model):
    name = models.CharField(max_length=300, null=False)
    national_id = models.IntegerField(unique=True, null=False)
    address = models.CharField(max_length=300)
    date_of_birth = models.DateTimeField(null=False)
    # gender = models.BoolenField()

class GeneralEntity(models.Model):
    name = models.CharField(max_length=300, null=False, default='entity')
    address = models.CharField(max_length=300)
    registration_num = models.CharField(max_length=300, unique=True)


class Clinic(GeneralEntity):
    pass

class Patient(GeneralUser):
    gender = models.CharField(max_length=100)
    mobile_num = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.name


class Prescription(GeneralUser):
    category = models.TextField(max_length=300)
    notes = models.TextField(max_length=300)
    prescribed_drugs = models.TextField(max_length=300)

    patient_info = models.ForeignKey('Patient', related_name='prescription_patient', on_delete=models.CASCADE)
    clinic = models.ForeignKey('Clinic', related_name='prescription_clinic', on_delete=models.CASCADE)
    pharmacy = models.ForeignKey('Pharmacy', related_name='prescription_pharmacy', on_delete=models.CASCADE)
    lab = models.ForeignKey('Laboratory', related_name='prescription_lab', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()


class Pharmacy(GeneralEntity):
    pass

class Laboratory(GeneralEntity):
    pass

class InsuranceCompany(GeneralEntity):
    pass
