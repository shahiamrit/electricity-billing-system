# Generated by Django 4.1.7 on 2023-02-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_001', '0009_addnewbillmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='addnewbillmodel',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
