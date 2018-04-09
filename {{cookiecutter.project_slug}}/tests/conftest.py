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
    """Provide an initialized Flask for use in certain test cases."""
    init_app(app, api)
    return app


@pytest.fixture(scope="session")
def client(application):
    """Provide a Flask test client to be used by almost all test cases."""
    with application.test_client() as client:
        yield client
