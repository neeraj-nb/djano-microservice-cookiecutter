#!/bin/sh
set -e 

python manage.py makemigrations
python manage.py migrate --noinput # no interaction
# python manage.py collectstatic --noinput

echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000 # replace the current shell with command