FROM python:latest
RUN mkdir /code
RUN apt-get update && apt-get install -y postgresql-client
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY UrlShortener /code/
WORKDIR /code/UrlShortener
CMD python manage.py migrate
CMD gunicorn UrlShortener.wsgi:application --bind 0.0.0.0:8000

