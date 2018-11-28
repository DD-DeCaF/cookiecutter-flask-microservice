# Copyright (c) 2018, Novo Nordisk Foundation Center for Biosustainability,
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

"""
Error handlers and custom exceptions.

http://flask.pocoo.org/docs/1.0/errorhandling/
http://flask.pocoo.org/docs/1.0/patterns/apierrors/
"""

import logging
import sys

from flask import jsonify

from werkzeug.exceptions import HTTPException
from werkzeug.routing import RoutingException


logger = logging.getLogger(__name__)


def init_app(app):
    @app.errorhandler(422)
    def handle_webargs_error(error):
        """
        Handle webargs parser errors.

        Ensures a JSON response including all error messages produced from the
        parser, that we know to be available on the error object.

        Note that this sets some constrains for manually throwing 422 exceptions
        as error messages must be made available in the same way.
        """
        response = jsonify(error.data['messages'])
        response.status_code = error.code
        return response

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        """
        Handle HTTPExceptions.

        Include the error description and corresponding status code, known to be
        available on the werkzeug HTTPExceptions.
        """
        # As werkzeug's routing exceptions also inherit from HTTPException,
        # check for those and allow them to return with redirect responses.
        if isinstance(error, RoutingException):
            return error
        else:
            response = jsonify({'message': error.description})
            response.status_code = error.code
            return response

    @app.errorhandler(Exception)
    def handle_uncaught_error(error):
        """
        Handle any uncaught exceptions.

        Since the handler suppresses the actual exception, log it explicitly to
        ensure it's logged and recorded in Sentry.

        Including the exception message would be helpful, but we would risk
        leaking sensitive information, so return a generic error message to the
        client.
        """
        logger.error("Uncaught exception", exc_info=sys.exc_info())
        response = jsonify({'message': "Internal server error"})
        response.status_code = 500
        return response
