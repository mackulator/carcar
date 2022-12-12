# Generated by Django 4.0.3 on 2022-12-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0003_alter_technician_employee_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=['%m/%d/%y %H:%M']),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='vin',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='technician',
            name='employee_number',
            field=models.PositiveIntegerField(),
        ),
    ]
