from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import ReserveSerializer, CabinetSerializer, WorkplaceSerializer
from .models import Booking, Workplace, Cabinet
from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser


class BookingAPIView(APIView):
    """Вывод списка бронирований по id рабочего места"""

    def get(self, request):
        booking = Booking.objects.all()
        serializer = ReserveSerializer(booking, many=True)
        return Response(serializer.data)


# #working
# class ReserveAPIView(APIView):
#     """Бронирование рабочих мест на определенный период времени"""
#
#     def put(self, request):
#         reserve = ReserveSerializer(data=request.data)
#         print(reserve)
#         if reserve.is_valid():
#             reserve.save()
#             print("valid")
#         else:
#             print(reserve.errors)
#             print("not valid")
#         return Response(reserve.data)


class ReserveView(viewsets.ModelViewSet):
    """Бронирование рабочих мест на определенный период времени"""
    queryset = Booking.objects.all()
    serializer_class = ReserveSerializer


class WorkplaceView(viewsets.ModelViewSet):
    """Бронирование рабочих мест на определенный период времени"""
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class CabinetView(viewsets.ModelViewSet):
    """Бронирование рабочих мест на определенный период времени"""
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
