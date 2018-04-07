FROM python:3.6-alpine

ENV PYTHONUNBUFFERED=1

ENV USER=giraffe

ARG UID=1000
ARG GID=1000

ARG INSTALL_PATH=/app

RUN addgroup -g "${GID}" -S "${USER}" && \
    adduser -u "${UID}" -S -G "${USER}" "${USER}"

RUN apk add --update --no-cache openssl ca-certificates

ENV PYTHONPATH="${INSTALL_PATH}/src"

WORKDIR "${INSTALL_PATH}"

COPY . "${INSTALL_PATH}/"

RUN chown -R "${USER}:${USER}" "${INSTALL_PATH}"

# `g++` is required for building `gevent` but all build dependencies are
# later removed again to reduce the layer size.
RUN apk add --no-cache --virtual .build-deps g++ \
    && pip install --upgrade pip setuptools wheel pipenv \
    && pipenv install --dev --system --deploy \
    && rm -rf /root/.cache/pip \
    && apk del .build-deps

