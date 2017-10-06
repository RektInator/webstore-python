@echo off
python manage.py dumpdata store > temp_data.json
python manage.py sqlclear store | python manage.py dbshell
python manage.py syncdb
python manage.py loaddata temp_data.json