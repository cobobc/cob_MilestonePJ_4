# Generated by Django 3.2 on 2022-02-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comments',
            field=models.TextField(max_length=2000),
        ),
    ]