# Generated by Django 3.0.8 on 2020-07-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
