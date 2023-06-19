from django.core.management.base import BaseCommand
from adventures.models import Adventure

class Command(BaseCommand):
    help = 'Remove all adventures'

    def handle(self, *args, **kwargs):
        Adventure.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All adventures were deleted successfully.'))
