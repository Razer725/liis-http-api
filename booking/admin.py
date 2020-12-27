from django.contrib import admin
from .models import Booking, Workplace, Cabinet


class BookingInline(admin.TabularInline):
    """Бронь"""
    model = Booking


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    """Кабинета"""
    list_display = ("cabinet_number",)


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    """Рабочее место"""
    inlines = [BookingInline, ]
    list_display = ('workplace_number', 'cabinet')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Бронь"""
    list_display = ("id", "workplace", "datetime_from", "datetime_to")
    list_display_links = ("workplace",)
