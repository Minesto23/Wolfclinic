# Generated by Django 3.1.5 on 2021-02-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210201_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('b+', 'b+'), ('b-', 'b-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='A+', max_length=3),
        ),
    ]
