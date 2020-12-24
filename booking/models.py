from django.db import models


class Cabinet(models.Model):
    room_number = models.PositiveIntegerField('Номер кабинета')


class Workplace(models.Model):
    number = models.PositiveIntegerField('Номер рабочего места')
    cabinet = models.ForeignKey(Cabinet, verbose_name='Кабинет', on_delete=models.CASCADE)


class Booking(models.Model):
    workplace = models.ForeignKey(Workplace, verbose_name='Рабочее место', on_delete=models.CASCADE)
    check_in = models.DateTimeField(verbose_name='Дата начала бронирования')
    check_out = models.DateTimeField(verbose_name='Дата окончания бронирования')
