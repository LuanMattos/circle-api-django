from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from photo_statistic.models import PhotoStatistic
from photo.models import Photo
from photo_statistic.serializer import PhotoStatisticSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.views import APIView



import pprint
pp = pprint.PrettyPrinter(indent=4)


class PhotoStatisticas(generics.ListAPIView):
    """Exibindo todas as estatisticas de photo e video """
    serializer_class = PhotoStatisticSerializer
    def get_queryset(self):
        queryset = PhotoStatistic.objects.filter(user_id=self.kwargs['pk'])
        return queryset
  
         

