# Generated by Django 3.1.3 on 2020-11-27 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0003_auto_20201108_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='auth_user_id',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
