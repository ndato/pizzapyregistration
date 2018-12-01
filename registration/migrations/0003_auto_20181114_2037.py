# Generated by Django 2.1 on 2018-11-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20181114_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='email',
            field=models.EmailField(error_messages={'required': 'Please provide your email address', 'unique': 'An entry with this email already exists'}, max_length=254, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Registered on'),
        ),
    ]