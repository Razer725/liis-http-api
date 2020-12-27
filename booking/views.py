from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import get_list_or_404

from .serializers import BookingSerializer, CabinetSerializer, WorkplaceSerializer, \
    ShowBookingSerializer, ShowFreeWorkplacesSerializer

from .models import Booking, Workplace, Cabinet


class BookingAPIView(APIView):
    """Бронирование рабочих мест на определенный период времени"""
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
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
        # booking = Booking.objects.filter(workplace=pk)
        booking = get_list_or_404(Booking, workplace=pk)
        serializer = ShowBookingSerializer(booking, many=True)
        return Response(serializer.data)


class ShowFreeWorkplacesAPIView(APIView):
    """
    Свободные рабочие места в указанный временной промежуток.
    Если временной промежуток не указан выводит список всех рабочих мест
    """

    def get(self, request):
        q = request.query_params
        start_date = q.get('datetime_from', None)
        end_date = q.get('datetime_to', None)

        queryset = Booking.objects.all()
        w = Workplace.objects.all().values('workplace_number')

        serializer = ShowFreeWorkplacesSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors)

        if start_date is not None and end_date is not None:
            queryset = queryset.filter(datetime_from__range=(start_date, end_date),
                                       datetime_to__range=(start_date, end_date))
            occupied_workplaces_id = queryset.values('workplace').distinct()
            to_exclude = [o['workplace'] for o in occupied_workplaces_id]
            w = w.exclude(workplace_number__in=to_exclude)
            return Response(w)
        elif start_date is not None:  # end_date=None
            queryset = queryset.filter(datetime_from__gt=start_date,
                                       datetime_to__gt=start_date)
            occupied_workplaces_id = queryset.values('workplace').distinct()
            to_exclude = [o['workplace'] for o in occupied_workplaces_id]
            w = w.exclude(workplace_number__in=to_exclude)
            return Response(w)
        elif end_date is not None:  # start_date=None
            queryset = queryset.filter(datetime_from__lt=end_date,
                                       datetime_to__lt=end_date)
            occupied_workplaces_id = queryset.values('workplace').distinct()
            to_exclude = [o['workplace'] for o in occupied_workplaces_id]
            w = w.exclude(workplace_number__in=to_exclude)
            return Response(w)
        return Response(w)
