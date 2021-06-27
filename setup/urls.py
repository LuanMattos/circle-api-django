from django.contrib import admin
from django.urls import path,include
from user.views import UsersViewSet
from photo.views import PhotosViewSet
from follower.views import FollowersViewSet
from like.views import LikesViewSet
from comment.views import CommentsViewSet
from photo_statistic.views import PhotoStatisticas
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Users')
router.register('photos', PhotosViewSet, basename='Photos')
router.register('likes', LikesViewSet, basename='Likes')
router.register('followers', FollowersViewSet, basename='Followers')
router.register('comments', CommentsViewSet, basename='Comments')
# router.register(r'photo_statistic/<int:pk>/', PhotoStatisticViewSet, basename='PhotoStatistic')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    # path('photo_statistic_start/<int:pk>/', StatisticStart.as_view()),
    # path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
    path('photo_statistic/<int:pk>/', PhotoStatisticas.as_view())
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
