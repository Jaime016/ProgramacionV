from django.core.management.base import BaseCommand
from libros.models import Libro

class Command(BaseCommand):
    help = "Lista los libros mejor calificados por género"

    def handle(self, *args, **kwargs):
        libros = Libro.objects.select_related('genero', 'calificacion')

        if not libros.exists():
            self.stdout.write("No hay libros cargados.")
            return

        # Agrupar por género
        generos = libros.values_list('genero__nombre', flat=True).distinct()

        for genero in sorted(set(generos)):
            self.stdout.write("\n" + "="*50)
            self.stdout.write(f"📚 Recomendaciones para género: {genero}")
            self.stdout.write("="*50)

            mejores = libros.filter(genero__nombre=genero).order_by('-calificacion__puntaje')[:5]
            for libro in mejores:
                self.stdout.write(f"• {libro.titulo} ({libro.calificacion.puntaje}/5) - Autor: {libro.autor.nombre}")
