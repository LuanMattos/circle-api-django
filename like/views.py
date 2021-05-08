from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from like.models import Like
from like.serializer import LikeSerializerV2, LikeSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class LikesViewSet(viewsets.ModelViewSet):
    """Exibe todos os Likes """
    queryset = Like.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return LikeSerializerV2
        else:
            return LikeSerializer