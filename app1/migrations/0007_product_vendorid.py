# Generated by Django 4.2.4 on 2023-08-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_vendorregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendorid',
            field=models.CharField(default='', max_length=200),
        ),
    ]
