from django.core.management.base import BaseCommand
from libros.models import Libro
from django.db.models import Avg

class Command(BaseCommand):
    help = 'Lista los libros mejor calificados por género'

    def handle(self, *args, **kwargs):
        generos = Libro.objects.values_list('genero__nombre', flat=True).distinct()
        self.stdout.write('📚 Recomendaciones de libros por género:\n')
        
        for genero in generos:
            libros = (
                Libro.objects
                .filter(genero__nombre=genero)
                .annotate(promedio=Avg('calificacion__puntaje'))
                .exclude(promedio__isnull=True)
                .order_by('-promedio')[:5]
            )
            
            self.stdout.write(f"🎯 Género: {genero}")
            if libros.exists():
                for libro in libros:
                    puntaje = libro.promedio if libro.promedio else 0
                    self.stdout.write(f"  - {libro.titulo} (Promedio: {puntaje:.2f})")
            else:
                self.stdout.write("  No hay libros en este género.")
            self.stdout.write("\n" + "-"*40 + "\n")
