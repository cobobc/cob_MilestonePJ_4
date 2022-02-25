# Generated by Django 3.2 on 2022-02-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0003_alter_beat_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='date published')),
                ('comment', models.TextField(max_length=2000)),
            ],
        ),
    ]
