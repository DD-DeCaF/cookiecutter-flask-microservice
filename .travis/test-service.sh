#!/usr/bin/env bash

set -eux

# Test the current state of the cookiecutter app and its configuration by
# creating a temporary service from the template and running the full QA suite
# in it. Note that the image builds on a wsgi-base image that has already
# passed QA, so we're not testing the dependencies here - just the code and
# configuration in the cookiecutter.

cookiecutter --no-input .
pushd "name-of-the-project"
git init
git add .
git commit -m "chore: create project template"
make lock
make build
make setup
make start
make qc
popd
