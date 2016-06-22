from rest_framework import serializers

from .models import Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        exclude = 'image_exterior', 'image_interior', 'image_floor_plan'


class AircraftDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
