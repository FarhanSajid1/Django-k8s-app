FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf*
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY django_project/static/ /static/
EXPOSE 80