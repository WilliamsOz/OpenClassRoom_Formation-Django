# Generated by Django 5.0.3 on 2024-04-02 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_listing_willy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='willy',
        ),
    ]