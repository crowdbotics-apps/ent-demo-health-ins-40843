# Generated by Django 2.2.28 on 2023-05-25 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20230525_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callcenter',
            name='patientId',
        ),
    ]
