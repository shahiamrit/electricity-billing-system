# Generated by Django 4.1.7 on 2023-02-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_001', '0002_rename_addcustomer_addcustomermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]