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

"""Provide settings for different deployment scenarios."""

import os


__all__ = ("Development", "Testing", "Production")


class Default(object):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DEBUG = True
        self.SECRET_KEY = os.urandom(24)
        self.LOGLEVEL = "DEBUG"
        self.CORS_ORIGINS = os.environ['ALLOWED_ORIGINS'].split(",")


class Development(Default):
    pass


class Testing(Default):
    pass


class Production(Default):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DEBUG = False
        self.SECRET_KEY = os.environ['SECRET_KEY']
        self.LOGLEVEL = "INFO"
