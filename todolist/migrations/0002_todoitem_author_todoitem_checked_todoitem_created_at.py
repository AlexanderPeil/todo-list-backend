# Generated by Django 4.2.7 on 2023-11-08 08:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
