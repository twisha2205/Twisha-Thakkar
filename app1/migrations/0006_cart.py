# Generated by Django 4.2.4 on 2023-08-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_sellerregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=250)),
                ('productid', models.CharField(max_length=250)),
                ('vendorid', models.CharField(max_length=250)),
                ('quantity', models.CharField(max_length=250)),
                ('totalprice', models.CharField(max_length=250)),
            ],
        ),
    ]