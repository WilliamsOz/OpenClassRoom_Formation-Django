# Generated by Django 5.0.3 on 2024-04-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_remove_band_like_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='willy',
            field=models.CharField(blank=True, max_length=42),
        ),
    ]
