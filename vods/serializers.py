from rest_framework import serializers
from .models import *


class VodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vod
        fields = "__all__"


class CreateVodSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    video = serializers.FileField()
    # Endpoint allows `belongs_to` to contain the pk of a user for attribution.
    belongs_to = serializers.CharField()
    played_by = serializers.CharField()
    map = serializers.CharField()
    winning_team = serializers.CharField()
    length = serializers.IntegerField()
    vod = serializers.IntegerField()

