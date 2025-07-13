from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Comando de prueba reportes'

    def handle(self, *args, **kwargs):
        self.stdout.write('¡Comando reportes funcionando!')
