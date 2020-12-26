from django.contrib import admin
from .models import Booking, Workplace, Cabinet


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Бронь"""
    list_display = ("workplace", "datetime_from", "datetime_to")
    list_display_links = ("workplace",)


@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    """Рабочее место"""
    list_display = ("workplace_number", "cabinet")
    list_display_links = ("cabinet", )


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    """Кабинет"""
    list_display = ("cabinet_number",)


# class BookingAdmin(admin.TabularInline):
#     """Бронь"""
#     model = Booking
#
#
# class WorkplaceAdmin(admin.ModelAdmin):
#     """Рабочее место"""
#     inlines = [BookingAdmin, ]
#
#
# class CabinetAdmin(admin.ModelAdmin):
#     """Кабинет"""
#     list_display = ("room_number",)

#
# admin.site.register(Booking)
# admin.site.register(Cabinet)
# admin.site.register(Workplace)
