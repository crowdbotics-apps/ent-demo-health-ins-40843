# Generated by Django 2.2.28 on 2023-05-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_callcenter_patientid'),
    ]

    operations = [
        migrations.AddField(
            model_name='callcenter',
            name='patientId',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='patientId',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]