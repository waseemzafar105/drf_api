# Generated by Django 3.2.16 on 2022-11-24 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplydetails',
            name='quantity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
