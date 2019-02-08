# {{cookiecutter.project_name}}

![master Branch](https://img.shields.io/badge/branch-master-blue.svg)
[![master Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![master Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master)

![devel Branch](https://img.shields.io/badge/branch-devel-blue.svg)
[![devel Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=devel)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![devel Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel)

## Post-cookiecutter steps

Perform the following steps after creating a new service from the cookiecutter.

* Create kubernetes secrets `{{cookiecutter.project_slug}}-production` and `{{cookiecutter.project_slug}}-staging`. Values needed:
  * `SECRET_KEY` (see [How to generate good secret keys](http://flask.pocoo.org/docs/1.0/quickstart/#sessions))
  * `SENTRY_DSN`
* Review the cpu/memory limits in `deployment/deployment.yml` under `resources` ([see documentation](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/))
* Create the following environment variables in Travis CI:
  * `ENVIRONMENT`: `testing`
  * `GCLOUD_EMAIL`: Google Cloud service account email for Travis CI
  * `GCLOUD_KEY`: Google Cloud service account key for Travis CI (JSON file base64-encoded)
* Generate secure token for Slack notifications in `.travis.yml`
  * [Install the Travis CLI](https://github.com/travis-ci/travis.rb#installation)
  * Run the following command in the project root directory:
    `travis encrypt "account:token#channel" --add notifications.slack.rooms`
* Remove this section from the README.

## Development

Run `make setup` first when initializing the project for the first time. Type
`make` to see all commands.

### Environment

Specify environment variables in a `.env` file. See `docker-compose.yml` for the
possible variables and their default values.

* Set `ENVIRONMENT` to either
  * `development`,
  * `testing`, or
  * `production`.
* `SECRET_KEY` Flask secret key. Will be randomly generated in development and testing environments.
* `SENTRY_DSN` DSN for reporting exceptions to
  [Sentry](https://docs.sentry.io/clients/python/integrations/flask/).
* `ALLOWED_ORIGINS`: Comma-seperated list of CORS allowed origins.

### Code style

In order of priority, code must adhere to the rules of the following tools:

1. [black](https://github.com/ambv/black)
2. [flake8](http://flake8.pycqa.org/en/latest/)
    * pycodestyle
    * pyflakes
    * mccabe
    * [pydocstyle](http://www.pydocstyle.org/en/2.1.1/index.html)
3. The [NumPy docstring standard](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
4. [isort](https://github.com/timothycrosley/isort)
