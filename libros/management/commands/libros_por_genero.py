from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Comando de prueba para libros_por_genero'

    def handle(self, *args, **kwargs):
        self.stdout.write("El comando libros_por_genero funciona correctamente")
