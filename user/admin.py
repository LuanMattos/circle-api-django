from django.contrib import admin
from user.models import User

class Users(admin.ModelAdmin):
    list_display = ('user_id','user_name')
    list_display_links = ('user_id', 'user_name')
    search_fields = ('user_name',)
    list_per_page = 20

admin.site.register(User, Users)

# class Cursos(admin.ModelAdmin):
#     list_display = ('id', 'codigo_curso', 'descricao')
#     list_display_links = ('id', 'codigo_curso')
#     search_fields = ('codigo_curso',)

# admin.site.register(Curso, Cursos)

# class Matriculas(admin.ModelAdmin):
#     list_display = ('id', 'aluno', 'curso', 'periodo')
#     list_display_links = ('id', )

# admin.site.register(Matricula, Matriculas)