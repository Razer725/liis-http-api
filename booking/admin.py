from django.contrib import admin
from .models import Booking, Workplace, Cabinet


# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     """Бронь"""
#     list_display = ("workplace", "datetime_from", "datetime_to")
#     list_display_links = ("workplace",)
#
#
# @admin.register(Workplace)
# class WorkplaceAdmin(admin.ModelAdmin):
#     """Номер рабочего места"""
#     list_display = ("workplace_number", "cabinet")
#     list_display_links = ("cabinet", )
#
#
# @admin.register(Cabinet)
# class CabinetAdmin(admin.ModelAdmin):
#     """Номер кабинета"""
#     list_display = ("cabinet_number",)



class BookingInline(admin.TabularInline):
    """Бронь"""
    model = Booking


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    """Рабочее место"""
    inlines = [BookingInline, ]
    list_display = ('id', 'workplace_number', 'cabinet')


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    """Кабинета"""
    list_display = ("cabinet_number",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Бронь"""
    list_display = ("id", "workplace", "datetime_from", "datetime_to")
    list_display_links = ("workplace", )
