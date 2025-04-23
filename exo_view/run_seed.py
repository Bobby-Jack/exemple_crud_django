import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'exo_view.settings')
django.setup()

from exo_app import seed

if __name__ == "__main__":
    seed.generate_product()