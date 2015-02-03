#!/bin/sh
python manage.py sqlclear teamfinder | python manage.py dbshell
python manage.py flush
python manage.py syncdb
