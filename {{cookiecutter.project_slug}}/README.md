# {{cookiecutter.project_name}}

<<<<<<< HEAD
![Branch](https://img.shields.io/badge/branch-master-blue.svg)
[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master)
[![Requirements Status](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=master)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=master)

![Branch](https://img.shields.io/badge/branch-devel-blue.svg)
[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=devel)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel)
[![Requirements Status](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=devel)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=devel)
=======
![master Branch](https://img.shields.io/badge/branch-master-blue.svg)
[![master Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![master Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master)
[![master Requirements Status](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=master)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=master)

![devel Branch](https://img.shields.io/badge/branch-devel-blue.svg)
[![devel Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=devel)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![devel Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel)
[![devel Requirements Status](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=devel)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=devel)
>>>>>>> chore: exchange readmes and fix slightly

## Development

Type `make` to see all commands.

### Environment

<<<<<<< HEAD
Specify environment variables in a `.env`. See `docker-compose.yml` for the
possible variables and their default values.

* `ENVIRONMENT` Set to either
  * `development`
  * `testing`
  * `production`
* `SECRET_KEY` Flask secret key. Will be randomly generated in dev/testing envs
* `SENTRY_DSN` DSN for reporting exceptions to [Sentry](https://docs.sentry.io/clients/python/integrations/flask/)
* `ALLOWED_ORIGINS`: Comma-seperated list of CORS allowed origins
=======
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
>>>>>>> chore: exchange readmes and fix slightly
