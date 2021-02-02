# Generated by Django 3.1.5 on 2021-02-01 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='medical_speciality',
            field=models.CharField(choices=[('ALL', 'Allergology'), ('ANE', 'Anesthesiology'), ('ANG', 'Angiology'), ('CAR', 'Cardiology'), ('END', 'Endocrinology'), ('STO', 'Stomatology'), ('GAS', 'Gastroenterology'), ('GER', 'Geriatrics'), ('HEM', 'Hematology'), ('HEP', 'Hepatology'), ('INF', 'Infectology'), ('AER', 'Aerospace medicine'), ('SPO', 'Sports medicine'), ('EME', 'Emergency medicine'), ('FAM', 'Family and community medicine'), ('PHY', 'Physical medicine and rehabilitation'), ('FOR', 'Forensic Medicine'), ('INT', 'Intensive medicine'), ('INM', 'Internal Medicine'), ('PRE', 'preventive medicine and public health'), ('WOR', 'Work Medicine'), ('NEP', 'Nephrology'), ('PNE', 'Pneumology'), ('NEU', 'Neurology'), ('NUT', 'Nutriology'), ('MED', 'Medical oncology'), ('RAD', 'Radiation Oncology'), ('PED', 'Pediatrics'), ('PSY', 'Psychiatry'), ('RHE', 'Rheumatology'), ('TOX', 'Toxicology')], default='ALL', max_length=3),
        ),
        migrations.AddField(
            model_name='doctor',
            name='turn',
            field=models.CharField(choices=[('1th', '1th Turn'), ('2nd', '2nd Turn'), ('3rd', '3rd Turn')], default='1th', max_length=3),
        ),
        migrations.AddField(
            model_name='floor',
            name='floor_name',
            field=models.CharField(choices=[('ALL', 'Allergology'), ('ANE', 'Anesthesiology'), ('ANG', 'Angiology'), ('CAR', 'Cardiology'), ('END', 'Endocrinology'), ('STO', 'Stomatology'), ('GAS', 'Gastroenterology'), ('GER', 'Geriatrics'), ('HEM', 'Hematology'), ('HEP', 'Hepatology'), ('INF', 'Infectology'), ('AER', 'Aerospace medicine'), ('SPO', 'Sports medicine'), ('EME', 'Emergency medicine'), ('FAM', 'Family and community medicine'), ('PHY', 'Physical medicine and rehabilitation'), ('FOR', 'Forensic Medicine'), ('INT', 'Intensive medicine'), ('INM', 'Internal Medicine'), ('PRE', 'preventive medicine and public health'), ('WOR', 'Work Medicine'), ('NEP', 'Nephrology'), ('PNE', 'Pneumology'), ('NEU', 'Neurology'), ('NUT', 'Nutriology'), ('MED', 'Medical oncology'), ('RAD', 'Radiation Oncology'), ('PED', 'Pediatrics'), ('PSY', 'Psychiatry'), ('RHE', 'Rheumatology'), ('TOX', 'Toxicology')], default='ALL', max_length=3),
        ),
    ]