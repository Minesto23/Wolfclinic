# Generated by Django 3.1.5 on 2021-02-01 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210201_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor'),
        ),
    ]
