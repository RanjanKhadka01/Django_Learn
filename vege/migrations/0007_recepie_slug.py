# Generated by Django 5.1.1 on 2024-10-03 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_reportcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepie',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 10, 3, 15, 25, 7, 264872, tzinfo=datetime.timezone.utc), unique=True),
            preserve_default=False,
        ),
    ]
