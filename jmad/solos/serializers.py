from django.utils.text import slugify

from rest_framework import serializers

from .models import Solo


class SoloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Solo
        read_only_fields = ('slug',)

    def validate(self, attrs):
        attrs['slug'] = slugify(attrs['artist'])
        return attrs
