from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('reserve', views.ReserveView)
router.register('workplace', views.WorkplaceView)
router.register('cabinet', views.CabinetView)

urlpatterns = [
    path('booking/', views.BookingAPIView.as_view()),
    path('', include(router.urls))
    # path('reserve/', views.ReserveView.as_view()),
    # path('workplace/', views.WorkplaceView.as_view()),
    # path('cabinet/', views.CabinetView.as_view()),
]
