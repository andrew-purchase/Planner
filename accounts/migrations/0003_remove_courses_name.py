# Generated by Django 3.1.2 on 2021-03-27 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210327_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='name',
        ),
    ]