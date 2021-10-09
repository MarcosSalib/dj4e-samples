from django.db import models

# Create your models here.


class GeneralUser(models.Model):
    name = models.CharField(max_length=300, null=False)
    address = models.CharField(max_length=300, null=False)
    date_of_birth = models.DateTimeField(null=False)
    national_id = models.IntegerField(unique=True)


class GeneralEntity(models.Model):
    name = models.CharField(max_length=300, null=False)
    address = models.CharField(max_length=300, null=False)

    registration_num = registration_num = models.CharField(max_length=300, unique=True)


class Clinic(GeneralEntity):
    pass

class Patient(GeneralUser):
    gender = models.CharField(max_length=100)
    mobile_num = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Prescription(GeneralUser):
    category = models.TextField(max_length=300)
    notes = models.TextField(max_length=300)
    prescribed_drugs = models.TextField(max_length=300)

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=False)
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE, null=False)
    pharmacy = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    lab = models.ForeignKey('Laboratory', on_delete=models.CASCADE)

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
