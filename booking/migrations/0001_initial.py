# Generated by Django 3.1.4 on 2020-12-24 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.PositiveIntegerField(verbose_name='Номер кабинета')),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Номер рабочего места')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.cabinet', verbose_name='Кабинет')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(verbose_name='Дата начала бронирования')),
                ('check_out', models.DateTimeField(verbose_name='Дата окончания бронирования')),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.workplace', verbose_name='Рабочее место')),
            ],
        ),
    ]
