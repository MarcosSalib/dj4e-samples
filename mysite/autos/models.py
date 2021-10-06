from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(
        max_length = 200,
        help_text = 'Enter the car manufacturer/brand',
        validators = [MinLengthValidator(2, 'Make must be greater than 1 character')]
    )
    origin = models.CharField(
        max_length=200,
        help_text='Enter the country of origin',
    )

    def __str__(self) -> str:
        return self.name


class Auto(models.Model):
    model = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, 'Car model must be greater than 1 character')]
    )
    shape = models.CharField(
        max_length=200,
        help_text='Enter body shape'
    )
    mileage = models.PositiveBigIntegerField()
    year = models.PositiveBigIntegerField()
    area = models.CharField(max_length=200)
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.model