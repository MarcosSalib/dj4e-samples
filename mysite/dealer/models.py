from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=300)
    clinic_address = models.CharField(max_length=300)
    national_id = models.IntegerField()
    registration_num = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=300)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=100)
    mobile_num = models.IntegerField()
    national_id = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Prescription(models.Model):
    category = models.TextField(max_length=300)
    notes = models.TextField(max_length=300)
    prescribed_drugs = models.TextField(max_length=300)

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=False)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, null=False)

    pharmacy = models.ForeignKey('Pharmacy', on_delete=models.CASCADE, null=False)
    lab = models.ForeignKey('Laboratory', on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return super().__str__()


class Pharmacy(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    registration_num = models.CharField(max_length=300)


class Laboratory(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    registration_num = models.CharField(max_length=300)
