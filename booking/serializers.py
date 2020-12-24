from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    # workplace = serializers.SlugRelatedField(slug_field='number', read_only=True)

    class Meta:
        model = Booking
        fields = ('workplace', 'check_in', 'check_out')
