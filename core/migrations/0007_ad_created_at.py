# Generated by Django 3.0.5 on 2020-04-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ad_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]