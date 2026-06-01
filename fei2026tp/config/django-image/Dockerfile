FROM python:3.12.2-bookworm

WORKDIR /usr/src/app

COPY ./config/django-image/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8000

COPY ./config/django-image/runserver.sh /scripts/runserver.sh
RUN chmod +x /scripts/runserver.sh

CMD ["/scripts/runserver.sh"]
