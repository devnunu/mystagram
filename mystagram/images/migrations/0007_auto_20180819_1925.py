# Generated by Django 2.0.7 on 2018-08-19 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20180819_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]
