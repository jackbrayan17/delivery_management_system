# Generated by Django 5.0.7 on 2024-08-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMS', '0008_alter_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
