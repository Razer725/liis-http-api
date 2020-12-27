from rest_framework import serializers
import io
from rest_framework.parsers import JSONParser
from .models import Booking, Workplace, Cabinet
import datetime


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = ('cabinet_number',)


class WorkplaceSerializer(serializers.ModelSerializer):
    cabinet = CabinetSerializer()

    class Meta:
        model = Workplace
        fields = ('workplace_number', 'cabinet')


class BookingSerializer(serializers.ModelSerializer):
    """Бронирование рабочего места"""

    # workplace = WorkplaceSerializer()

    def validate(self, data):
        if data['datetime_from'] > data['datetime_to']:
            raise serializers.ValidationError('Дата начала бронирования должна быть раньше окончания')
        if Booking.objects.filter(datetime_from__range=(data['datetime_from'], data['datetime_to']),
                                  workplace=data['workplace']):
            raise serializers.ValidationError('В указанный промежуток времени уже есть запись')
        if Booking.objects.filter(datetime_to__range=(data['datetime_from'], data['datetime_to']),
                                  workplace=data['workplace']):
            raise serializers.ValidationError('В указанный промежуток времени уже есть запись')
        return data

    def create(self, validated_data):
        print(validated_data, 'validated data')
        booking = Booking.objects.all()

        start_date = validated_data['datetime_from']
        end_date = validated_data['datetime_to']
        print(start_date, 'start date')
        print(end_date, 'end date')
        print(start_date < end_date)

        print(booking, 'all')
        booking = Booking.objects.create(**validated_data)
        return booking

    class Meta:
        model = Booking
        fields = ('workplace', 'datetime_from', 'datetime_to')


class ShowBookingSerializer(serializers.ModelSerializer):
    """Список бронирований по id рабочего места"""

    class Meta:
        depth = 1
        model = Booking
        fields = ('workplace', 'datetime_from', 'datetime_to')


class ShowFreeWorkplacesSerializer(serializers.ModelSerializer):
    """Список свободных рабочих мест в указанный промежуток времени"""
    datetime_from = serializers.DateTimeField(required=False)
    datetime_to = serializers.DateTimeField(required=False)

    def validate(self, data):
        if 'datetime_from' in data and 'datetime_to' in data:
            if data['datetime_from'] > data['datetime_to']:
                raise serializers.ValidationError('Дата начала бронирования должна быть раньше окончания')
        return data

    class Meta:
        model = Booking
        fields = ('datetime_from', 'datetime_to')
