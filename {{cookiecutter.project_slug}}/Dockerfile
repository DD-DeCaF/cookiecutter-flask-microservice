FROM python:3.6-alpine

ARG INSTALL_PATH=/app

WORKDIR ${INSTALL_PATH}

COPY Pipfile* ${INSTALL_PATH}/

# `g++` is required for building `gevent` but all build dependencies are
# later removed again to reduce the layer size.
RUN apk add --no-cache --virtual .build-deps g++ \
    && pip install pipenv \
    && pipenv install --system --deploy \
    && rm -rf /root/.cache/pip \
    && apk del .build-deps

CMD ["gunicorn", "-c", "gunicorn.py", "{{cooiecutter.project_slug}}.wsgi:app"]
