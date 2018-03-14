# {{cookiecutter.project_name}}

![Branch](https://img.shields.io/badge/branch-master-blue.svg)
[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master)
[![Requirements Status](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=master)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=master)

![Branch](https://img.shields.io/badge/branch-devel-blue.svg)
[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=devel)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel)
[![Requirements Status](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=devel)](https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=devel)

## Development

Type `make` to see all commands.

### Environment

Specify environment variables in a `.env`. See `docker-compose.yml` for the
possible variables and their default values.

* `ENVIRONMENT` Set to either
  * `development`
  * `testing`
  * `production`
