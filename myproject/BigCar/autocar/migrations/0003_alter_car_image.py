# Generated by Django 3.2.12 on 2024-04-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocar', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='car_images'),
        ),
    ]
