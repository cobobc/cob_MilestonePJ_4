# Generated by Django 3.2 on 2022-02-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0008_auto_20220224_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
    ]
