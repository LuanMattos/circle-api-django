from rest_framework import viewsets, generics, status
from follower.models import Follower
from follower.serializer import FollowerSerializer

class FollowersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os usuários """
    queryset = Follower.objects.all()
    def get_serializer_class(self):
        return FollowerSerializer
    
