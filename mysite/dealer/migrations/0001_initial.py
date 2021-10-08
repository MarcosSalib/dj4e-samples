# Generated by Django 3.2.7 on 2021-10-08 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('clinic_address', models.CharField(max_length=300)),
                ('national_id', models.IntegerField()),
                ('registration_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('registration_num', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(max_length=100)),
                ('mobile_num', models.IntegerField()),
                ('national_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('registration_num', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(max_length=300)),
                ('notes', models.TextField(max_length=300)),
                ('prescribed_drugs', models.TextField(max_length=300)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.doctor')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.laboratory')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.patient')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.pharmacy')),
            ],
        ),
    ]
