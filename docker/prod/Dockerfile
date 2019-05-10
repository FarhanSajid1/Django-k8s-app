FROM python:3.7-alpine

WORKDIR /app
COPY requirements/ .

RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip install -r prod.txt

# Add entrypoint script
COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh

COPY ./ ./

EXPOSE 8990

ENTRYPOINT ["entrypoint.sh"]

WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=django_project.settings.production PGUSER=postgres\
      PGHOST=postgres\
      PGDATABASE=postgres\
      PGPASSWORD=postgres_password\
      PGPORT=5432\
      GOOGLE_PASSWORD=${GOOGLE_PASSWORD}\
      GOOGLE_USER=${GOOGLE_USER}\
      AWS_STORAGE_BUCKET_NAME=${AWS_STORAGE_BUCKET_NAME}\
      AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}\
      AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}\
      DJANGO_SETTINGS_MODULE=django_project.settings.production\
      USE_S3=TRUE\
      SECRET_KEY='afoiajsfoija84284uijskflkamlfkmaskfjaofjoa'


# This is the command for setting up the gunicorn webserver
CMD gunicorn -w 4 -b 0.0.0.0:8990 django_project.wsgi --env DJANGO_SETTINGS_MODULE=django_project.settings.production




















