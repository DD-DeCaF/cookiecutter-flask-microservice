FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

ARG INSTALL_PATH=/app

ARG UID=1000
ARG GID=1000

RUN addgroup -g ${GID} -S giraffe && \
    adduser -u ${UID} -S giraffe -G giraffe

WORKDIR ${INSTALL_PATH}

COPY . ${INSTALL_PATH}/

# `g++` is required for building `gevent` but all build dependencies are
# later removed again to reduce the layer size.
RUN apk add --no-cache --virtual .build-deps g++ \
    && pip install pipenv \
    && pipenv install --dev --system --deploy \
    && rm -rf /root/.cache/pip \
    && apk del .build-deps

USER giraffe
