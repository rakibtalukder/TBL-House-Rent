# Generated by Django 3.0.5 on 2020-10-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='agreementid',
            field=models.CharField(default=False, max_length=30),
        ),
    ]