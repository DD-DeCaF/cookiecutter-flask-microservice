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

import logging
import os

from flask import Flask
from flask_restplus import Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(
    title="{{cookiecutter.project_name}}",
    version="0.1.0",
    description="{{cookiecutter.project_short_description}}",
)


def init_app(application, interface):
    if os.environ["ENVIRONMENT"] == "production":
        from {{cookiecutter.project_module}}.settings import Production
        application.config.from_object(Production())
    elif os.environ["ENVIRONMENT"] == "testing":
        from {{cookiecutter.project_module}}.settings import Testing
        application.config.from_object(Testing())
    else:
        from {{cookiecutter.project_module}}.settings import Development
        application.config.from_object(Development())

    # Configure the logger and handler.
    application.logger.setLevel(application.config["LOGLEVEL"])
    formatter = logging.Formatter("[%(levelname)s] [%(name)s] %(message)s")
    for handler in application.logger.handlers:
        handler.setFormatter(formatter)

    # Set the logging level and add handlers to desired packages here.
    # FIXME: Remove those that are too spammy and uninteresting.
    cors_logger = logging.getLogger("flask_cors")
    cors_logger.setLevel(application.config["LOGLEVEL"])
    for handler in application.logger.handlers:
        cors_logger.addHandler(handler)

    # Add routes and resources.
    from {{cookiecutter.project_module}} import resources
    interface.add_resource(resources.HelloWorld, "/")
    interface.init_app(application)

    # Add CORS information for all resources.
    CORS(application)
