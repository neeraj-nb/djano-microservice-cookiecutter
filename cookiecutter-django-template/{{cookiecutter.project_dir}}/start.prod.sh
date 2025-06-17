#!/bin/sh
set -e 

echo "Starting Gunicorn..."

exec gunicorn user_service.wsgi:application --bind 0.0.0.0:8000