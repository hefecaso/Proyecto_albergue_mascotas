# syntax=docker/dockerfile:1
FROM python:3.8.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
COPY librerias.txt /code/

RUN pip install -r librerias.txt
COPY . /code/

EXPOSE 8000

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "Albergue_mascotas", "Albergue_mascotas.wsgi:application"]
