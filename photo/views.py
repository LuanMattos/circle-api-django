from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from photo.models import Photo
from photo.serializer import PhotoSerializerV2, PhotoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class PhotosViewSet(viewsets.ModelViewSet):
    """Exibe todas as fotos """
    queryset = Photo.objects.all()
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return PhotoSerializerV2
        else:
            return PhotoSerializer

# Create your views here.
