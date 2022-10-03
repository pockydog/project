FROM python:3.8-slim
MAINTAINER vickychen@fillygaming888.com
LABEL version = '1.0'

ARG PRODUCT_NAME='app'
RUN mkdir -p /${PRODUCT_NAME}
WORKDIR /${PRODUCT_NAME}


COPY src .
WORKDIR /app
COPY requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt