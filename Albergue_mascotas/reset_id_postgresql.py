import os

os.environ['DJANGO_COLORS'] = 'nocolor'

from django.core.management import call_command
from django.db import connection
from django.apps import apps
from io import StringIO

commands = StringIO()
cursor = connection.cursor()

for app in apps.get_app_configs():
    call_command('sqlsequencereset', app.label, stdout=commands)

cursor.execute(commands.getvalue())
