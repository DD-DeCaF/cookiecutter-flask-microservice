# Copyright (c) {{cookiecutter.year}}, Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Provide session level fixtures."""

import pytest

from {{cookiecutter.project_module}}.app import api, app, init_app


@pytest.fixture(scope="session")
def application():
    init_app(app, api)
    with app.app_context():  # FIXME: Is this necessary?
        yield app


@pytest.fixture(scope="session")
def client(application):
    with application.test_client() as client:
        yield client
