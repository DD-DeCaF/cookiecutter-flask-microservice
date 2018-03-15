{{cookiecutter.project_name}}
==============================

|Master Branch| |Master Build Status| |Master Codecov| |Master Requirements Status|

|Devel Branch| |Devel Build Status| |Devel Codecov| |Devel Requirements Status|

Development
-----------

* Type ``make`` to see all commands.
* After installing versioneer you need to set it up:
  * ``versioneer install``

Environment
-----------

Specify environment variables in a ``.env``. See ``docker-compose.yml``
for the possible variables and their default values.

-  ``ENVIRONMENT`` Set to either
-  ``"development"``
-  ``"testing"``
-  ``"production"``
-  ``SECRET_KEY`` Flask secret key. Will be randomly generated in
   dev/testing envs

.. |Master Branch| image:: https://img.shields.io/badge/branch-master-blue.svg
.. |Master Build Status| image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master
   :target: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
.. |Master Codecov| image:: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master
.. |Master Requirements Status| image:: https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=master
   :target: https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=master
.. |Devel Branch| image:: https://img.shields.io/badge/branch-devel-blue.svg
.. |Devel Build Status| image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=devel
   :target: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
.. |Devel Codecov| image:: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/devel
.. |Devel Requirements Status| image:: https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements.svg?branch=devel
   :target: https://requires.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/requirements/?branch=devel
