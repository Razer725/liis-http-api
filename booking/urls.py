from django.urls import path, include

from . import views

urlpatterns = [
    path('booking/', views.BookingAPIView.as_view()),
    path('show-booking/<int:pk>/', views.ShowBookingAPIView.as_view()),
    path('workplace/', views.WorkplaceAPIView.as_view()),
    path('cabinet/', views.CabinetAPIView.as_view()),
    path('free-workplaces/', views.ShowFreeWorkplacesAPIView.as_view())
]
