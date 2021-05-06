from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
# class CursoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Curso
#         fields = '__all__'

# class MatriculaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Matricula
#         exclude = []

# class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
#     curso = serializers.ReadOnlyField(source='curso.descricao')
#     periodo = serializers.SerializerMethodField()
#     class Meta:
#         model = Matricula
#         fields = ['curso', 'periodo']
#     def get_periodo(self, obj):
#         return obj.get_periodo_display()

# class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
#     aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
#     class Meta:
#         model = Matricula
#         fields = ['aluno_nome']

# # -------------------- Versões 2 --------------------
class UserSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name']