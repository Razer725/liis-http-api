from django.contrib import admin
from .models import Booking, Workplace, Cabinet


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Бронь"""
    list_display = ("workplace", "check_in", "check_out")


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    """Рабочее место"""
    list_display = ("number", "cabinet")


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    """Кабинет"""
    list_display = ("room_number",)
