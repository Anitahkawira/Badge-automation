#!/bin/sh

#alembic upgrade head
echo "Starting application service server"
# Run Service
python manage.py runserver 0.0.0.0:8000