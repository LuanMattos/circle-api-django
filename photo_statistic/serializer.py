from rest_framework import serializers
from photo_statistic.models import PhotoStatistic
from photo.models import Photo
from photo.serializer import PhotoSerializer

class PhotoStatisticSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(required=True)
    class Meta:
        model = PhotoStatistic
        fields = '__all__'
    