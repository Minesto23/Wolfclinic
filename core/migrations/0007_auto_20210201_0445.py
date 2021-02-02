# Generated by Django 3.1.5 on 2021-02-01 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_patient_blood_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='A+', max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.doctor'),
        ),
    ]