# Generated by Django 2.1.4 on 2021-11-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstagramApp', '0016_auto_20211101_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
