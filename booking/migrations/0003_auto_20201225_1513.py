# Generated by Django 3.1.4 on 2020-12-25 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20201225_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabinet',
            old_name='room_number',
            new_name='cabinet_number',
        ),
        migrations.RenameField(
            model_name='workplace',
            old_name='number',
            new_name='workplace_number',
        ),
        migrations.AlterUniqueTogether(
            name='workplace',
            unique_together={('workplace_number', 'cabinet')},
        ),
    ]
