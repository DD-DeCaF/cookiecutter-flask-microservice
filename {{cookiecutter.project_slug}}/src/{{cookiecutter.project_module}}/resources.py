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

"""Implement RESTful API endpoints using resources."""

import warnings

from flask_apispec import MethodResource, marshal_with, use_kwargs
from flask_apispec.extension import FlaskApiSpec

from .schemas import HelloSchema


def init_app(app):
    """Register API resources on the provided Flask application."""

    def register(path, resource):
        app.add_url_rule(path, view_func=resource.as_view(resource.__name__))
        with warnings.catch_warnings():
            # Silence the following warning:
            #   apispec/ext/marshmallow/common.py:145: UserWarning: Multiple
            #   schemas resolved to the name Organism. The name has been
            #   modified. Either manually add each of the schemas with a
            #   different name or provide a custom schema_name_resolver.
            # This happens due to `exclude` usage in the schema which makes
            # apispec create a new model, and that's the correct behaviour.
            warnings.simplefilter("ignore")
            docs.register(resource, endpoint=resource.__name__)

    docs = FlaskApiSpec(app)
    app.add_url_rule("/healthz", view_func=healthz)
    register("/hello", HelloResource)


def healthz():
    """
    Return an empty, successful response for readiness checks.

    A successful response signals that the app is initialized and ready to
    receive traffic. The main use case is for apps with slow initialization, but
    external dependencies like database connections can also be tested here.
    """
    return ""


class HelloResource(MethodResource):
    """Example API resource."""

    @use_kwargs(HelloSchema)
    @marshal_with(HelloSchema, code=200)
    def get(self, name):
        """
        Implement example endpoint.

        This demonstrates both how to use request argument validation
        (use_kwargs) and response marshalling (marshal_with).
        """
        return {"name": name}
