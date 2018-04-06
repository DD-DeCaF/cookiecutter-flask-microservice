FROM python:3.6-alpine

ENV PYTHONUNBUFFERED=1

ENV USER=giraffe

ARG UID=1000
ARG GID=1000

ARG PWD=/app

RUN addgroup -g "${GID}" -S "${USER}" && \
    adduser -u "${UID}" -S -G "${USER}" "${USER}"

RUN apk add --update --no-cache openssl ca-certificates

WORKDIR "${PWD}"

COPY . "${PWD}/"

RUN chown -R "${USER}:${USER}" "${PWD}"

# `g++` is required for building `gevent` but all build dependencies are
# later removed again to reduce the layer size.
# The symlink is a temporary workaround for a bug in pipenv.
# Still present as of pipenv==11.9.0.
RUN set -x \
    && ln -sf /usr/local/bin/python /bin/python \
    && apk add --no-cache --virtual .build-deps g++ \
    && pip install --upgrade pip setuptools wheel pipenv \
    && pipenv install --dev --system --deploy \
    && rm -rf /root/.cache/pip \
    && apk del .build-deps

