from django.contrib import admin
from django.urls import path,include
from user.views import UsersViewSet
from photo.views import PhotosViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Users')
router.register('photos', PhotosViewSet, basename='Photos')
# router.register('cursos', CursosViewSet, basename='Cursos')
# router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    # path('users/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    # path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
