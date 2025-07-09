from rest_framework import serializers
from .models import Autor, Genero, Calificacion, Libro


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

#reajuste para cuando se elimine en el ṕostman se reutilice la numeracion nuevamente 
class LibroSerializer(serializers.ModelSerializer):

    numero = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ['numero', 'id', 'titulo', 'autor', 'genero', 'calificacion']

    def get_numero(self, obj):
        # 'index' viene del contexto de la vista
        return self.context.get('index', 0)