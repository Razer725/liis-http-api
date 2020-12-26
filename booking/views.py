from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from .serializers import BookingSerializer, CabinetSerializer, WorkplaceSerializer, \
    ShowBookingSerializer, ShowFreeWorkplacesSerializer
from .models import Booking, Workplace, Cabinet
from rest_framework.decorators import api_view
from django.db.models.options import Options
import io
from rest_framework.parsers import JSONParser


# working
class BookingAPIView(APIView):
    """Бронирование рабочих мест на определенный период времени"""

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            print("valid")
            return Response(serializer.data, status=201)
        print("not valid")
        return Response(serializer.errors, status=400)


class WorkplaceAPIView(APIView):

    def get(self, request):
        booking = Workplace.objects.all()
        serializer = WorkplaceSerializer(booking, many=True)
        return Response(serializer.data)


class CabinetAPIView(APIView):

    def get(self, request):
        booking = Cabinet.objects.all()
        serializer = CabinetSerializer(booking, many=True)
        return Response(serializer.data)


class ShowBookingAPIView(APIView):
    """Просмотр списка бронирований по id рабочего места"""

    def get(self, request, pk):
        booking = Booking.objects.filter(workplace=pk)
        serializer = ShowBookingSerializer(booking, many=True)
        return Response(serializer.data)


# class ShowFreeWorkplacesAPIView(APIView):
#     """Свободные рабочие места в указанный временной промежуток"""
#
#     # def get(self, request):
#     #     return
#
#     def get(self, request):
#         print(request.query_params)
#         q = request.query_params
#         start_date = q.get('datetime_from', None)
#         end_date = q.get('datetime_to', None)
#
#         queryset = Booking.objects.all()
#         serializer = ShowFreeWorkplacesSerializer(queryset, many=True)
#         # if start_date:
#         #     queryset = queryset.filter(datetime_from__lt=start_date)
#         # if end_date:
#         #     queryset = queryset.filter(datetime_to__gt=end_date)
#         # print(queryset)
#         return Response(serializer.data)


class ShowFreeWorkplacesAPIView(generics.ListAPIView):
    """Свободные рабочие места в указанный временной промежуток"""

    serializer_class = ShowFreeWorkplacesSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Booking.objects.all()

        start_time = self.request.query_params.get('datetime_from', None)
        end_time = self.request.query_params.get('datetime_to', None)
        # queryset = Workplace.objects.all()
        # print(queryset)
        if start_time is not None and end_time is not None:
            queryset = queryset.filter(datetime_from__range=(start_time, end_time),
                                       datetime_to__range=(start_time, end_time))
            print(queryset.values('workplace'), 'filtered queryset')

        occupied_workplaces_id = queryset.values('workplace')
        print(occupied_workplaces_id, 'occupied workplaces')
        free_workplaces = Booking.objects.exclude(workplace__in=occupied_workplaces_id)
        print(free_workplaces, 'free workplaces')
        # if datetime_from is not None:
        #     queryset = queryset.exclude(datetime_from__range=(queryset['datetime_from'], queryset['datetime_to']))
        #     print(queryset, 'filter1')
        # if datetime_to is not None:
        #     queryset = queryset.filter(datetime_to__gt=datetime_to)
        return free_workplaces.distinct()


