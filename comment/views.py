from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from comment.models import Comment
from comment.serializer import CommentSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CommentsViewSet(viewsets.ModelViewSet):
    """Exibe todos os comentários """
    queryset = Comment.objects.all()
    def get_serializer_class(self):
        return CommentSerializer