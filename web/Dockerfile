FROM python:3.6.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ARG APP_ENV=dev
ADD . /code/
RUN pip install -r requirements/${APP_ENV}.txt