# Generated by Django 4.2.14 on 2024-08-01 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_date']},
        ),
    ]