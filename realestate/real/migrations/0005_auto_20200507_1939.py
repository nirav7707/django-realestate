# Generated by Django 3.0.5 on 2020-05-07 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0004_auto_20200504_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qfield',
            old_name='owner_email',
            new_name='owner_name',
        ),
        migrations.RenameField(
            model_name='qfield',
            old_name='qmaker_city',
            new_name='your_city',
        ),
        migrations.RenameField(
            model_name='qfield',
            old_name='qmaker_name',
            new_name='your_name',
        ),
    ]
