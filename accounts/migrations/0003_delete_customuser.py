# Generated by Django 5.1.1 on 2024-10-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
