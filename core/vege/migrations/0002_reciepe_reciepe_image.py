# Generated by Django 5.1.7 on 2025-04-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepe',
            name='reciepe_image',
            field=models.ImageField(blank=True, null=True, upload_to='reciepe'),
        ),
    ]
