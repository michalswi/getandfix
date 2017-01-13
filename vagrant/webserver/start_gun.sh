#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn django_app.wsgi:application \
    --bind 127.0.0.1:8080 \
    --workers 3
