from rest_framework import serializers
from like.models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        #exclude = []

# # -------------------- Versões 2 --------------------
class LikeSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'