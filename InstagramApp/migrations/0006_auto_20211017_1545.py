# Generated by Django 2.1.4 on 2021-10-17 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InstagramApp', '0005_auto_20211017_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='InstagramApp.Profile'),
        ),
    ]
