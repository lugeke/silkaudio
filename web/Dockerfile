FROM python:3.6.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN pip install -r requirements/prod.txt