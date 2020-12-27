from django.db import models


class Cabinet(models.Model):
    cabinet_number = models.PositiveIntegerField('Номер кабинета', primary_key=True)

    def __str__(self):
        return str(self.cabinet_number)


class Workplace(models.Model):
    workplace_number = models.PositiveIntegerField('Номер рабочего места', primary_key=True)
    cabinet = models.ForeignKey(Cabinet, verbose_name='Кабинет', on_delete=models.CASCADE,
                                related_name='cabinet')

    def __str__(self):
        return str(self.workplace_number)


class Booking(models.Model):
    workplace = models.ForeignKey(Workplace, verbose_name='Рабочее место', on_delete=models.CASCADE,
                                  related_name='workplaces')
    datetime_from = models.DateTimeField(verbose_name='Дата начала бронирования')
    datetime_to = models.DateTimeField(verbose_name='Дата окончания бронирования')

