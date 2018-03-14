#!/usr/bin/env bash

# Copyright (c) {{cookiecutter.year}}, Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -euv

REPO="{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}"
GIT_MASTER_HEAD_SHA=$(git rev-parse --short=12 --verify HEAD)
BRANCH=$TRAVIS_BRANCH

docker build -f Dockerfile -t $REPO:$BRANCH .
docker tag $REPO:$BRANCH $REPO:$GIT_MASTER_HEAD_SHA
docker push $REPO:$BRANCH
docker push $REPO:$GIT_MASTER_HEAD_SHA
if [ BRANCH = "master" ]; then
   docker tag $REPO:$BRANCH $REPO:latest
   docker push $REPO:latest
fi
