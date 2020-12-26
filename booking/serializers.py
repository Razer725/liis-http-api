from rest_framework import serializers
import io
from rest_framework.parsers import JSONParser
from .models import Booking, Workplace, Cabinet


class CabinetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cabinet
        fields = ('cabinet_number', )


class WorkplaceSerializer(serializers.ModelSerializer):
    cabinet = CabinetSerializer()

    class Meta:
        model = Workplace
        fields = ('id', 'workplace_number', 'cabinet')

#working
# class ReserveSerializer(serializers.ModelSerializer):
#     """Бронирование рабочего места"""
#     # cabinet = serializers.IntegerField(source='workplace.workplace_number')
#
#     #test
#     workplace = serializers.PrimaryKeyRelatedField(queryset=Workplace.objects.all())
#     cabinet = serializers.PrimaryKeyRelatedField(queryset=Cabinet.objects.all())
#
#     # owner = PrimaryKeyRelatedField(queryset=User.objects.all())
#
#     def create(self, validated_data):
#         booking = Booking.objects.update_or_create(
#             workplace=validated_data.get('workplace'),
#             defaults={'datetime_from': validated_data.get('datetime_from'),
#                       'datetime_to': validated_data.get('datetime_to')}
#         )
#         return booking
#
#     class Meta:
#         model = Booking
#         fields = ('workplace', 'datetime_from', 'datetime_to', 'cabinet')


class ReserveSerializer(serializers.ModelSerializer):
    """Бронирование рабочего места"""
    workplace = WorkplaceSerializer()

    class Meta:
        model = Booking
        fields = ('workplace', 'datetime_from', 'datetime_to')



