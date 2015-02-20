#!/bin/bash
python manage.py dumpdata teamfinder > temp_data.json
python manage.py sqlclear teamfinder | python manage.py dbshell
python manage.py syncdb
python manage.py loaddata temp_data.json
