FROM python:3.9.4
RUN mkdir app
WORKDIR /src/app

LABEL description='Development image for booking app on DRF + ReactJS'

ENV PYTHONUNBUFFERED 1

COPY req.txt /src/backend

RUN pip install --upgrade pip && pip install -r req.txt
COPY . /src/app
RUN npm install && npm run build


EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]