from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('reserve', views.ReserveView)
# router.register('workplace', views.WorkplaceView)
# router.register('cabinet', views.CabinetView)

urlpatterns = [
    path('booking/', views.BookingAPIView.as_view()),
    # path('', include(router.urls))
    path('show-booking/<int:pk>/', views.ShowBookingAPIView.as_view()),
    path('workplace/', views.WorkplaceAPIView.as_view()),
    path('cabinet/', views.CabinetAPIView.as_view()),
    path('free-workplaces/', views.ShowFreeWorkplacesAPIView.as_view())
]
