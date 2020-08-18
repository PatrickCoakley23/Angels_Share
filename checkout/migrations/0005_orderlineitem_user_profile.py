# Generated by Django 3.1 on 2020-08-18 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile'),
        ),
    ]