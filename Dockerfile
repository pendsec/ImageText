FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /imagetext

WORKDIR /imagetext

RUN apt-get update && apt-get install -y \
    libsasl2-dev \
    python3-dev \
    libldap2-dev \
    libssl-dev \
    libcairo2-dev \
    pango1.0-tests \
    libxml2-dev \
    libxmlsec1-dev \
    libxmlsec1-openssl \
 && rm -rf /var/lib/apt/lists/*

ADD . /imagetext/

RUN apt-get update && apt-get install -y python3-dev && pip install -r imagetext/requirements/testing.txt
