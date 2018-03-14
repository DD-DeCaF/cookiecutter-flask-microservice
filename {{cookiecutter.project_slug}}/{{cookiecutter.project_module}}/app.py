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

"""Expose the main Flask-RESTPlus application."""

import os

from flask import Flask
from flask_restplus import Api

import {{cookiecutter.project_module}}.resources as resources
import {{cookiecutter.project_module}}.settings as settings


app = Flask(__name__)
api = Api(
    title="{{cookiecutter.project_name}} API",
    version="0.1.0",
    description="{{cookiecutter.project_short_description}}",
    doc="/docs"  # FIXME: Should be disabled in production.
)


def init_app(application: Flask, interface: Api):
    if os.environ["ENVIRONMENT"] == "production":
        application.config.from_object(settings.Production)
    elif os.environ["ENVIRONMENT"] == "testing":
        application.config.from_object(settings.Testing)
    else:
        application.config.from_object(settings.Development)
    interface.add_resource(resources.HelloWorld, "/")
    interface.init_app(application)
