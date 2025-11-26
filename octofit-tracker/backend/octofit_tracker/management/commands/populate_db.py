from django.core.management.base import BaseCommand
import os
import sys


class Command(BaseCommand):
    help = 'Populate octofit_db with test data (wrapper for scripts/populate_db.py)'

    def handle(self, *args, **options):
        # Ensure scripts path is available
        backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        scripts_dir = os.path.abspath(os.path.join(backend_dir, '..', 'scripts'))
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)

        try:
            from scripts.populate_db import populate
        except Exception as e:
            self.stderr.write(f'Failed to import populate: {e}')
            return

        populate()
        self.stdout.write(self.style.SUCCESS('octofit_db populated'))
