from rest_framework import serializers

from .models import Solo


class SoloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solo
