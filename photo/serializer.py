from rest_framework import serializers
from photo.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

# # -------------------- Versões 2 --------------------
class PhotoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo_id', 'photo_url']