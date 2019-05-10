#!/bin/sh


echo "applying database migrations"

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

echo "starting server"

exec $@


