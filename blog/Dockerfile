FROM python:3.10
RUN mkdir app
RUN mkdir app/static
RUN mkdir app/media
RUN mkdir app/downloads
WORKDIR /src/app

LABEL description='Development image for Blog prototype using DRF'

ENV PYTHONUNBUFFERED 1

COPY req.txt /src/app

RUN pip install --upgrade pip && pip install -r req.txt
COPY . /src/app

EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]