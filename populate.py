#setting up the Django environment
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","P6.settings")

#setting up the django platform
import django
django.setup()

from myapp.models import *
import random
